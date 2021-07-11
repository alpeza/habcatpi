prinstep(){
    set +x
    echo '*************************************************'
    echo  "STEP $1 -> $2"
    echo '*************************************************'
}

prinstep '0' 'Update de repositorios ...'
sudo apt-get update

prinstep '1' 'Instalando git ...'
set -x
sudo apt-get install -y git 
set +x

prinstep '2' 'Instalando MQTT ...'
set -x
sudo apt-get install -y mosquitto mosquitto-clients
sudo systemctl status mosquitto
set +x

prinstep '3' 'Instalando NPM ...'
set -x
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v
sudo npm install -g pm2 
sudo pm2 startup
set +x

prinstep '5' 'Descargando librerias de habcat ...'
set -x
pip3 install habcatev
set +x

prinstep '6' 'Creando estructura de carpetas ...'
cd $HOME
mkdir habcat
cd habcat
mkdir components
mkdir mydevices
cd $HOME

prinstep '7' 'Rebooting ...'
set -x
sudo reboot
set +x