import json
from json import *
from datetime import *
from datetime import date
def create_event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    d = {
       'org': org,'event_id':Event_ID,
       'event_name':Event_Name,
       'start_date':Start_Date,
       'start_time':Start_Time,
       'end_date':End_Date,
       'end_time':End_Time,
       'user':Users_Registered,
       'capacity':Capacity,
       'availability':Availability
    }

    f = open(events_json_file,'r+')
    try:
        content = json.load(f)
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
    except json.decoder.JSONDecodeError:
        l = []
        l.append(d)
        json.dump(l,f)
    f.close()

def view_event(org,events_json_file):
    org = input()
    f = open(events_json_file,'r')
    for sub in f:
        if sub['org']==org:
            print(sub.items())
    f.close()

def view_event_ByID(events_json_file,Event_ID):
    Event_ID = input()
    f=open(events_json_file,'r')
    for sub in f:
        if sub["Event_ID"]==Event_ID:
            print(sub.items())
    f.close()

def Update_Event(org,events_json_file,event_id,details_to_be_updated,updated_detail):
    event_id = input()
    f = open(events_json_file,'r+')
    content = json.load(f)
    for sub in f:
        if sub['Event_ID']== event_id:
            details_to_be_updated = {
                                    'org':org,
                                    'event_id':event_id
                                    }
            f = open(events_json_file,'r+')
            json.dump(details_to_be_updated,f)
            return True
        else:
            return False
    f.close()

def Delete_Event(org,events_json_file,event_ID):
    event_ID = input()
    f = open(events_json_file,'r+')
    content = json.load(f)
    for sub in f:
        if sub["Event_ID"]==event_ID:
            content.pop(sub)
def Register_for_Event(events_json_file,event_id,Full_Name):
    date_today = str(date.today())
    now= datetime.now()
    current_time = now.strftime('%H:%M:%S')
    event_id = input()
    f = open(events_json_file,'r+')
    content = json.load(f)
    for sub in f:
        if sub['Event_ID'] == event_id:
            d = {
                'Full_Name': Full_Name
            }
            f = open(events_json_file,'w')
            json.dump(d,f)
            return True
        else:
            return False
    f.close()

def Update_Password(members_json_file,Full_Name,new_password):
    Full_Name = input()
    f = open(members_json_file,'r')
    content = json.load(f)
    for sub in f:
        if sub["Full_Name"] == Full_Name:
            new_password = input()
            sub.update(new_password)
            return True
        else:
            return False
    f.close()

def View_all_events(events_json_file):
    content = None
    with open(events_json_file,'r+') as f:
        content = json.load(f)
        return content



