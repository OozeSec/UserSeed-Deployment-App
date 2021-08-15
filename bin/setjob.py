#############################
#    Author: Blake Putnam.  #
#    Date: 20210814.        #
#    Version: 1.0.0         #
#############################
"""
This script is created to set cron entries
for Userseed TA.
"""

from os import system as sh

sh('cat <(fgrep -i -V "/opt/splunkforwarder/etc/apps/userseed_deployment_app/bin/User-Seed-Generator.py" <(crontab -l)) <(echo "15 * * * *") | crontab -')
# setting cronjob for User-Seed-Generator.py
sh('cat <(fgrep -i -V "/opt/splunkforwarder/etc/apps/userseed_deployment_app/bin/cleanup.py" <(crontab -l)) <(echo "20 * * * *") | crontab -')
# setting cronjob for cleanup.py