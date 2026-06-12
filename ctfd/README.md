# CTFd Deployment

CTFd + MariaDB on a GCP e2-medium VM, with nginx TLS termination via Let's Encrypt.

Can run alongside a StealthOps TRAINING_MODE instance on the same VM (e2-medium is sufficient for both at classroom scale).

## Prerequisites

- GCP e2-medium (or equivalent) with a static external IP
- DNS A record pointing your domain to that IP
- Ubuntu 22.04 LTS

## 1. Install dependencies

```bash
sudo apt update && sudo apt install -y docker.io docker-compose-v2 nginx certbot python3-certbot-nginx
sudo systemctl enable --now docker nginx
sudo usermod -aG docker $USER   # log out and back in after this
```

## 2. Get TLS certificate

```bash
sudo certbot --nginx -d YOUR_DOMAIN
```

Certbot will modify nginx automatically for the initial cert. We'll replace the nginx config in the next step.

## 3. Clone repo and configure

```bash
git clone https://github.com/presack/eureka-labs.git
cd eureka-labs/ctfd
```

Create your environment file:

```bash
cat > .env <<EOF
SECRET_KEY=$(openssl rand -hex 32)
DB_PASSWORD=$(openssl rand -hex 24)
DB_ROOT_PASSWORD=$(openssl rand -hex 24)
EOF
```

Keep `.env` out of version control — it contains your database credentials.

## 4. Configure nginx

Replace `YOUR_DOMAIN` in `nginx.conf` with your actual domain:

```bash
sed -i 's/YOUR_DOMAIN/ctf.yourdomain.com/g' nginx.conf
sudo cp nginx.conf /etc/nginx/sites-available/ctfd
sudo ln -sf /etc/nginx/sites-available/ctfd /etc/nginx/sites-enabled/ctfd
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t && sudo systemctl reload nginx
```

## 5. Start CTFd

```bash
docker compose up -d
```

CTFd binds to `127.0.0.1:8000` only — nginx proxies public traffic to it.

Check logs:

```bash
docker compose logs -f ctfd
```

## 6. Initial CTFd setup

Open `https://YOUR_DOMAIN` in a browser. The setup wizard will ask for:
- Event name, description, start/end times
- Admin account credentials

Choose **Teams** or **Users** mode depending on whether students compete solo or in groups.

## 7. Import challenges

In the CTFd admin panel:
**Admin → Import/Export → Import**

Upload `challenges/osint/school-proxy/ctfd/challenges.yml`.

Verify all 10 challenges imported correctly under the **OSINT - School Proxy** category.

## 8. Configure CTFd settings

Recommended settings for classroom use:
- **Visibility:** Public (or registration-required)
- **Registration:** Token-based (distribute tokens to students)
- **Scoring:** Dynamic or static — static is simpler for a first deployment
- **Hints:** Enabled, costs as configured in the import file

## Maintenance

```bash
# Restart CTFd
docker compose restart ctfd

# View recent logs
docker compose logs --tail=100 ctfd

# Backup CTFd data (uploads + database dump)
docker compose exec db mysqldump -u ctfd -p ctfd > backup_$(date +%Y%m%d).sql

# Update CTFd image
docker compose pull && docker compose up -d
```

## Running alongside StealthOps

If StealthOps TRAINING_MODE is also running on this VM:
- StealthOps typically runs on port 3000 or 8080 — no conflict with CTFd on 8000
- Add a second nginx `server` block for the StealthOps domain, proxying to its port
- Both services share the MariaDB instance or run separate containers — your call

## Firewall

Only ports 22, 80, and 443 need to be open externally. CTFd's port 8000 should remain bound to `127.0.0.1` as configured in docker-compose.yml.

```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```
