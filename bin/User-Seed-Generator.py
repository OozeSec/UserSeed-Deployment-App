#############################
#    Author: Blake Putnam.  #
#    Date: 20210814.        #
#    Version: 1.0.0         #
#############################
"""
This script is to kick off the proccess
of staging the user-seed.conf to
$SPLUNK_HOME/etc/system/local/.
It also checks for the presence of passwd.conf
in $SPLUNK_HOME/etc/.
Once staging is completed the script replaces 
the default inputs.conf with a disabled attribute
for the script stanza to prevent potential loops.
"""

from os import system as sh

sh('echo "`date`,action=Starting...." >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/log/UDA.log')
# first write
sh('/opt/splunk/bin/splunk hash-passwd `cat /opt/splunkforwarder/etc/apps/userseed_deployment_app/admin/passwd.txt` >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/admin/swap.txt | echo "HASHED_PASSWORD = `cat /opt/splunkforwarder/etc/apps/userseed_deployment_app/admin/swap.txt | tail -1`" >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/conf/user-seed.conf')
# splunk generates a hashed password and it gets moved around a bit
sh('cp /opt/splunkforwarder/etc/apps/userseed_deployment_app/conf/user-seed.conf /opt/splunkforwarder/etc/system/local/')
# begin process
sh('echo "`date`,action=Verifying...."  >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/log/UDA.log | ls /opt/splunkforwarder/etc/system/local/ | grep user-seed >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/log/UDA.log')
# begin verification write and process
sh('echo "`date`,passwd=`ls /opt/splunkforwarder/etc | grep passwd`" >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/log/UDA.log')
# verify password.conf in $SPLUNK_HOME/etc/
sh('echo "`date`,action=ReplacingDefaultInputs(disabled)...." >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/log/UDA.log')
# begin removal write
sh('yes| mv /opt/splunkforward/etc/apps/userseed_deployment_app/default/inputs.conf.disabled /opt/splunkforward/etc/apps/userseed_deployment_app/default/inputs.conf | mv /opt/splunkforward/etc/apps/userseed_deployment_app/admin/passwd.txt.blank /opt/splunkforward/etc/apps/userseed_deployment_app/admin/passwd.txt | mv /opt/splunkforward/etc/apps/userseed_deployment_app/admin/swap.txt.blank mv /opt/splunkforward/etc/apps/userseed_deployment_app/admin/swap.txt')
# begin remove process
sh('echo "`date`,action=Completed...." >> /opt/splunkforwarder/etc/apps/userseed_deployment_app/log/UDA.log')
# last write, completion