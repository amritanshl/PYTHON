import os 
import datetime
import time
import schedule

name = ['EY','Accenture','HCL','Apple','Microsoft']


def job():
    mode = 0o666
    for x in name:
        year_f = str(datetime.datetime.now().year)
        month_f= str(datetime.datetime.now().month)
        day_f= str(datetime.datetime.now().day)
        hour_f= str(datetime.datetime.now().hour)
        min_f= str(datetime.datetime.now().minute)
        sec_f= str(datetime.datetime.now().second)

        # print(year_f,month_f,day_f,hour_f,min_f,sec_f)

        fileName = x+year_f+month_f+hour_f+min_f+sec_f

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
    if os.path.exists(os.path.join(month_path,day_f)):
        day_path = os.path.join(month_path,day_f)
    else:
        day_path = os.path.join(month_path,day_f)
        os.mkdir(day_path,mode)
    if os.path.exists(os.path.join(day_path,hour_f)):
        hour_path = os.path.join(day_path,hour_f)
    else:
        hour_path = os.path.join(day_path,hour_f)
        os.mkdir(hour_path,mode)
        

    if os.path.exists(os.path.join(hour_path,min_f)):
        min_path = os.path.join(hour_path,min_f)
    else:
        min_path = os.path.join(hour_path,min_f)
        os.mkdir(min_path,mode)
    if os.path.exists(os.path.join(min_path,sec_f)):
        sec_path = os.path.join(min_path,sec_f)
    else:
        sec_path = os.path.join(min_path,sec_f)
        os.mkdir(sec_path,mode)
    
    os.mkdir(os.path.join(sec_path,fileName),mode)


         


        #file_create = open(fileName,'w')
schedule.every().second.do(job)

while 1: 
    schedule.run_pending()
    time.sleep(2)
    


