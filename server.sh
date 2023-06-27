#!/bin/sh


while true
do
    host=`python3 api.py`

    echo ${host}

    # host=$1

    #  -o PubkeyAcceptedKeyTypes=ssh-rsa 
    scp  -tt -o PubkeyAcceptedKeyTypes=ssh-rsa ./run.sh  $host:"/root"
    scp  -tt -o PubkeyAcceptedKeyTypes=ssh-rsa ./docker-compose.yml  $host:"/root"

    ssh  -tt -o PubkeyAcceptedKeyTypes=ssh-rsa $host 'apk add screen && screen -d -m bash run.sh' 

    # # ubuntu setting
    # PROXY_STRING="socks://localhost:1080/"
    # export socks_proxy=$PROXY_STRING
    # export SOCKS_PROXY=$PROXY_STRING

    # gsettings set org.gnome.system.proxy mode 'manual';
    # gsettings set org.gnome.system.proxy.socks host "'localhost'";
    # gsettings set org.gnome.system.proxy.socks port 8000;

    # apt_conf_proxy="
    # Acquire::socks::Proxy \"$PROXY_STRING\";
    # "
    # echo "$apt_conf_proxy" | sudo tee /etc/apt/apt.conf.d/proxy > /dev/null

    # echo "Proxy enabled."
    # ###


    ssh -tt -o PubkeyAcceptedKeyTypes=ssh-rsa -o GatewayPorts=true  -L 8000:localhost:1080  $host

    # echo "" > /etc/apt/apt.conf.d/proxy 
done