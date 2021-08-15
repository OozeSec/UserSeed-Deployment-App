#############################
#    Author: Blake Putnam.  #
#    Date: 20210814.        #
#    Version: 1.0.0         #
#############################
"""
This script is created to remove cron entries
created from Userseed TA
Leaving no trace or jobs from its existence.
"""

from os import system as sh

sh('crontab -l | grep -v userseed_deployment_app | crontab -')
# scrub jobs
sh('echo "`date`,script=RemovingCron...." >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/log/UDA.log')
# print
sh('echo "`date`,script=`crontab -l`" >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/log/UDA.log') 
# verify
sh('echo "`date`,script=RestartingSplunkd...." >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/log/UDA.log | /opt/splunkforwarder/bin/splunk restart')
# restart splunkd