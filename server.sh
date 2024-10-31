#!/bin/sh

host=$1
type=$2
httppass=$3
port=$4
echo $type
echo ${host}
echo $port

loop="false"
while true
do
    if [ "$host" == "api-based" ]
    then
        host=`python3 api.py`
        loop="true"
    fi

    scp  -o PubkeyAcceptedKeyTypes=ssh-rsa ./run.sh ./passwords ./squid.conf  $host:/root

    if [ "$type" == "socks" ]
    then
        if [ "$httppass" == "no-pass" ]
        then
            scp  -o PubkeyAcceptedKeyTypes=ssh-rsa ./docker-compose-no-pass.yml  $host:/root/docker-compose.yml
        else
            scp  -o PubkeyAcceptedKeyTypes=ssh-rsa ./docker-compose.yml  $host:/root/docker-compose.yml
        fi
    else
        if [ "$httppass" == "no-pass" ]
        then
            scp  -o PubkeyAcceptedKeyTypes=ssh-rsa ./docker-compose-squid.yml  $host:/root/docker-compose.yml
            scp  -o PubkeyAcceptedKeyTypes=ssh-rsa ./squid-open.conf  $host:/root/squid.conf
        else
            scp  -o PubkeyAcceptedKeyTypes=ssh-rsa ./docker-compose-squid.yml  $host:/root/docker-compose.yml
        fi
    fi

    ssh   -o PubkeyAcceptedKeyTypes=ssh-rsa $host 'apk add screen && screen -d -m bash run.sh' 

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


    timeout --foreground  3h ssh  -o PubkeyAcceptedKeyTypes=ssh-rsa -o GatewayPorts=true  -L $port:localhost:1080  $host

    # echo "" > /etc/apt/apt.conf.d/proxy 

    if [ "$loop" != true ]
    then
        echo "breaking from the loop."
        break
    fi
    
    echo "timeout. reconnecting ..."
    sleep 5

done
