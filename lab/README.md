# Lab
This is a mini lab set made o be studying a bit about with a couple of friends

## Tools 
- Wiregurd vpn
- Docker

# Instalation
Have docker installed.

I've used a made easy wireguard installation on docker. [wg-easy](https://github.com/wg-easy/wg-easy)
Run this to setup your wireguard vpn
```
docker run -d \
  --name=wg-easy \
  -e WG_HOST=your-server-ip \
  -e PASSWORD=yourpassword \
  -v ~/.wg-easy:/etc/wireguard \
  -p 51820:51820/udp \
  -p 51821:51821/tcp \
  --cap-add=NET_ADMIN \
  --cap-add=SYS_MODULE \
  --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
  --sysctl="net.ipv4.ip_forward=1" \
  --restart unless-stopped \
  weejewel/wg-easy
```

Login to wireguard, and set up the connections for the containers and users that should access the lab. Download the configs and setup the docker compose according to the configs yur created.

Run the ```docker-compose up -d```
