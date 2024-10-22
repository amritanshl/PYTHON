import os
import sys
import datetime


mode = 0o666
year_f = str(datetime.datetime.now().year)
month_f= str(datetime.datetime.now().month)
day_f= str(datetime.datetime.now().day)
hour_f= str(datetime.datetime.now().hour)
min_f= str(datetime.datetime.now().minute)
sec_f= str(datetime.datetime.now().second)
year_path = os.path.join(os.getcwd(),'files',year_f)
get_current_directory = os.path.exists(year_path)

print(year_path)

if(os.path.exists(year_path)):
    print('Year exist')
else:
    os.mkdir(year_path,mode)

if os.path.exists(os.path.join(year_path,month_f)):
    month_path = os.path.join(year_path,month_f)
else:
    month_path = os.path.join(year_path,month_f)
    os.mkdir(month_path,mode)

if os.path.exists(os.path.join(month_path,sec_f)):
    sec_path = os.path.join(month_path,sec_f)
else:
    sec_path = os.path.join(month_path,sec_f)
    os.mkdir(sec_path,mode)





