awk '!/AllowTcpForwarding|GatewayPorts|X11Forwarding/' /etc/ssh/sshd_config > tmp.txt && mv tmp.txt /etc/ssh/sshd_config

echo -e "AllowTcpForwarding yes \nGatewayPorts yes \nX11Forwarding yes" >> /etc/ssh/sshd_config

kill $(pgrep ssh)
/usr/sbin/sshd -o PermitRootLogin=yes 


# echo "---\nversion: "2.1"\nservices:\n    socks5:\n        image: serjs/go-socks5-proxy\n        container_name: socks5\n        ports:\n          - 1080:1080" > docker-compose.yml

docker compose up -d 

