Install
=======

apt-get install python-software-properties python-dev python-pip
apt-get install libffi-dev libssl-dev  # for pySSL
pip install virtualenvwrapper
mkvirtualenv dashboard
git clone ...
pip install -r requirements.txt
copy local/production settings from example files
configure settings
install cron
wget http://s3.amazonaws.com/influxdb/influxdb_latest_amd64.deb
sudo dpkg -i influxdb_latest_amd64.deb
install grafana

Production
==========
configure nginx reverse proxy to access influxdb API (needed by grafana)
