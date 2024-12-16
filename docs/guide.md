# ICTAZ Notice Page Deployment Guide

This guide provides instructions for deploying the ICTAZ Notice Page on Ubuntu 18.04.

## Prerequisites

1. Ubuntu 18.04 server
2. Python 3.6 or higher
3. pip (Python package manager)
4. nginx web server

## Installation Steps

### 1. Update System Packages

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Install Required System Packages

```bash
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools nginx python3-venv -y
```

### 3. Create Project Directory

```bash
mkdir -p /var/www/ictazNotice
cd /var/www/ictazNotice
```

### 4. Set Up Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Gunicorn

Create a systemd service file:

```bash
sudo nano /etc/systemd/system/ictazNotice.service
```

Add the following content:

```ini
[Unit]
Description=Gunicorn instance to serve ICTAZ Notice
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/ictazNotice
Environment="PATH=/var/www/ictazNotice/venv/bin"
ExecStart=/var/www/ictazNotice/venv/bin/gunicorn --workers 3 --bind unix:ictazNotice.sock -m 007 app:app

[Install]
WantedBy=multi-user.target
```

### 7. Configure Nginx

Create an Nginx configuration file:

```bash
sudo nano /etc/nginx/sites-available/ictazNotice
```

Add the following content:

```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/ictazNotice/ictazNotice.sock;
    }
}
```

Create symbolic link:

```bash
sudo ln -s /etc/nginx/sites-available/ictazNotice /etc/nginx/sites-enabled
```

### 8. Start and Enable Services

```bash
sudo systemctl start ictazNotice
sudo systemctl enable ictazNotice
sudo systemctl restart nginx
```

### 9. Configure Firewall (if enabled)

```bash
sudo ufw allow 'Nginx Full'
```

## SSL Configuration (Optional but Recommended)

To secure your site with SSL using Let's Encrypt:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your_domain.com
```

## Maintenance

### Restarting Services

```bash
sudo systemctl restart ictazNotice
sudo systemctl restart nginx
```

### Viewing Logs

```bash
sudo journalctl -u ictazNotice
sudo tail -f /var/log/nginx/error.log
```

## Troubleshooting

1. Check if Gunicorn is running:
```bash
sudo systemctl status ictazNotice
```

2. Check Nginx configuration:
```bash
sudo nginx -t
```

3. Check permissions:
```bash
sudo chown -R www-data:www-data /var/www/ictazNotice
```
