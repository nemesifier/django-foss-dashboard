Install
=======

pip install virtualenvwrapper
mkvirtualenv dashboard
git clone ...
apt-get install libffi-dev  # for pySSL
pip install -r requirements.txt
copy local/production settings from example files
configure settings
install cron
install influxdb
install grafana

Production
==========
configure nginx reverse proxy to access influxdb API (needed by grafana)
