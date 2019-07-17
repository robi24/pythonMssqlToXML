# pythonMssqlToXML
Simple script to get a data from MSSQL server and parse it to a XML file

## run script
`make`

## installation
Use `make install` to install all required packages. `ubuntuDepInstall` is to install `ubuntu` dependencies

## add to CronTab
Run script every 1 minute
```
from crontab import CronTab

cron = CronTab(user='username')  # linux way
job = cron.new(command='python example1.py')  
job.minute.every(1)

cron.write() 
```
https://stackabuse.com/scheduling-jobs-with-python-crontab/

## todo
* [ ] add secrets and test sql server connection
* [ ] implement a proper XML schema
* [x] explore python-crontab
