#!/usr/bin/env python3
"""
Import all challenge sets into a running CTFd instance via the API.

Usage:
    python tools/import_challenges.py --token YOUR_API_TOKEN [--url http://localhost:8000]

Get a token from CTFd admin panel: Admin → Settings → Access Tokens → Generate

Handles two YAML layouts automatically:
  - One challenge.yml per subdirectory  (school-proxy format)
  - Single combined challenges.yml list  (kabelo-motsumi format)
"""

import os
import sys
import glob
import argparse

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: pip install pyyaml requests")

try:
    import requests
except ImportError:
    sys.exit("Missing dependency: pip install pyyaml requests")


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHALLENGE_SETS = [
    {
        "label": "OSINT - School Proxy",
        "dir_challenges": os.path.join(REPO_ROOT, "challenges", "osint", "school-proxy", "ctfd"),
    },
    {
        "label": "Forensics - Kabo Seretse",
        "file_challenges": os.path.join(REPO_ROOT, "challenges", "forensics", "kabelo-motsumi", "ctfd", "challenges.yml"),
    },
]


def headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def api(method, base_url, token, path, **kwargs):
    url = f"{base_url.rstrip('/')}{path}"
    resp = getattr(requests, method)(url, headers=headers(token), **kwargs)
    try:
        data = resp.json()
    except Exception:
        resp.raise_for_status()
        return {}
    if not resp.ok:
        msg = data.get("message") or data.get("errors") or resp.text
        raise RuntimeError(f"API error {resp.status_code} on {path}: {msg}")
    return data.get("data", data)


def load_dir_challenges(ctfd_dir):
    """Load individually-filed challenges (one challenge.yml per subdir)."""
    challenges = []
    for yml_path in sorted(glob.glob(os.path.join(ctfd_dir, "*/challenge.yml"))):
        with open(yml_path, encoding="utf-8") as f:
            challenges.append(yaml.safe_load(f))
    return challenges


def load_file_challenges(yml_path):
    """Load a combined challenges.yml list."""
    with open(yml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, list) else [data]


def import_challenge_set(base_url, token, challenges, label):
    print(f"\n{'='*60}")
    print(f"  {label}  ({len(challenges)} challenges)")
    print(f"{'='*60}")

    name_to_id = {}
    pending_prereqs = {}

    for ch in challenges:
        name = ch["name"]
        ctype = ch.get("type", "standard")

        payload = {
            "name": name,
            "category": ch.get("category", ""),
            "description": ch.get("description", ""),
            "value": ch.get("value", 0),
            "type": ctype,
            "state": ch.get("state", "visible"),
        }

        try:
            result = api("post", base_url, token, "/api/v1/challenges", json=payload)
        except RuntimeError as exc:
            if "manual" in str(exc).lower() or "type" in str(exc).lower():
                print(f"  ⚠  {name}: 'manual' type not supported, retrying as standard")
                payload["type"] = "standard"
                result = api("post", base_url, token, "/api/v1/challenges", json=payload)
            else:
                print(f"  ✗  {name}: {exc}")
                continue

        ch_id = result["id"]
        name_to_id[name] = ch_id

        # Flags
        for flag in ch.get("flags", []):
            api("post", base_url, token, "/api/v1/flags", json={
                "challenge_id": ch_id,
                "type": flag.get("type", "static"),
                "content": flag["content"],
                "data": flag.get("data", ""),
            })

        # Hints
        for hint in ch.get("hints", []):
            api("post", base_url, token, "/api/v1/hints", json={
                "challenge_id": ch_id,
                "type": "standard",
                "content": hint["content"],
                "cost": hint.get("cost", 0),
            })

        # Stash prerequisites for second pass
        prereqs = (ch.get("requirements") or {}).get("prerequisites", [])
        if prereqs:
            pending_prereqs[ch_id] = prereqs

        flag_count = len(ch.get("flags", []))
        hint_count = len(ch.get("hints", []))
        print(f"  ✓  [{ch_id:>3}] {name}  ({ch.get('value')} pts, {flag_count} flag(s), {hint_count} hint(s))")

    # Second pass: wire prerequisites now that all IDs are known
    if pending_prereqs:
        print("\n  Setting prerequisites...")
        for ch_id, prereq_names in pending_prereqs.items():
            ids = [name_to_id[n] for n in prereq_names if n in name_to_id]
            missing = [n for n in prereq_names if n not in name_to_id]
            if missing:
                print(f"    ⚠  Challenge {ch_id}: could not resolve prerequisites {missing}")
            if ids:
                api("patch", base_url, token, f"/api/v1/challenges/{ch_id}",
                    json={"requirements": {"prerequisites": ids}})

    return name_to_id


def main():
    parser = argparse.ArgumentParser(description="Import CTFd challenge sets from YAML")
    parser.add_argument("--url", default="http://localhost:8000", help="CTFd base URL (default: http://localhost:8000)")
    parser.add_argument("--token", required=True, help="CTFd API token (Admin → Settings → Access Tokens)")
    args = parser.parse_args()

    # Quick connectivity check
    try:
        resp = requests.get(f"{args.url.rstrip('/')}/api/v1/challenges", headers=headers(args.token))
        if resp.status_code == 403:
            sys.exit("Auth failed — check your token.")
        if not resp.ok:
            sys.exit(f"CTFd returned {resp.status_code}. Is it running at {args.url}?")
    except requests.ConnectionError:
        sys.exit(f"Cannot reach CTFd at {args.url}. Is the container running?")

    print(f"Connected to CTFd at {args.url}")

    for cs in CHALLENGE_SETS:
        if "dir_challenges" in cs:
            if not os.path.isdir(cs["dir_challenges"]):
                print(f"\nSkipping {cs['label']}: directory not found ({cs['dir_challenges']})")
                continue
            challenges = load_dir_challenges(cs["dir_challenges"])
        else:
            if not os.path.isfile(cs["file_challenges"]):
                print(f"\nSkipping {cs['label']}: file not found ({cs['file_challenges']})")
                continue
            challenges = load_file_challenges(cs["file_challenges"])

        if not challenges:
            print(f"\nSkipping {cs['label']}: no challenges found")
            continue

        import_challenge_set(args.url, args.token, challenges, cs["label"])

    print("\nDone.")


if __name__ == "__main__":
    main()
