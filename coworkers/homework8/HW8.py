import datetime
from datetime import datetime , timedelta

users = [
    {'name': 'Andry' ,'birthday': '2022-12-15'},
    {'name': 'Dima'  ,'birthday': '2022-12-16'},
    {'name': 'Billy' ,'birthday': '2022-12-17'},
    {'name': 'Snow'  ,'birthday': '2022-12-18'},
    {'name': 'Elena' ,'birthday': '2022-12-19'},
    {'name': 'Sasha' ,'birthday': '2022-12-20'},
    {'name': 'Diana' ,'birthday': '2022-12-21'},
    {'name': 'Kristi','birthday': '2022-12-22'},
    {'name': 'Roman' ,'birthday': '2022-12-23'},
    {'name': 'Jek' ,'birthday': '2022-12-15'},
    {'name': 'Carl'  ,'birthday': '2022-12-16'},
    {'name': 'Denis' ,'birthday': '2022-12-17'},
    {'name': 'Megan'  ,'birthday': '2022-12-18'},
    {'name': 'Joe' ,'birthday': '2022-12-19'},
    {'name': 'Tyler' ,'birthday': '2022-12-20'},
    {'name': 'Adriana' ,'birthday': '2022-12-21'},
    {'name': 'Nikita','birthday': '2022-12-22'},
    {'name': 'Nazar' ,'birthday': '2022-12-23'},
    
]

def birthday(users):
    dict_birthdays ={ #пробував додавати видразу в словник значення. чомусь не виходило. тому виришив робити черес списки
        "Monday"   : "nobody",
        "Thuesday" : "nobody",
        "Wednesdey": "nobody",
        "Thursday" : "nobody",
        "Friday"   : "nobody",
    }
    # роблю через списки, бо через словник помилки видае
    monday_list = []
    thuesday_list = []
    wednesday_list = []
    thursday_list = []
    friday_list = []

    seven_days = 7
    
    current_tim = datetime.now()
    current_time = current_tim.date()
    
    time_end = current_time + timedelta(days=seven_days)
    
    for user in users:
        date_clear = datetime.strptime(user["birthday"], "%Y-%m-%d")
        date_clear = date_clear.date()
        date_clear = date_clear.replace(year=current_time.year)
        if current_time <= date_clear <= time_end:
            #тут мабуть можна зробити все в 2 рази коротше
            if date_clear.weekday() == 0:
                monday_list.append(user["name"])
                
            elif date_clear.weekday() == 1:
                thuesday_list.append(user["name"])
            
            elif date_clear.weekday() == 2:
                wednesday_list.append(user["name"])
                
            elif date_clear.weekday() == 3:
                thursday_list.append(user["name"])
                
            elif date_clear.weekday() == 4:
                friday_list.append(user["name"])
                
            elif date_clear.weekday() == 5 or 6:
                monday_list.append(user["name"])
      # и тут мабуть теж можна зробити все в 2 рази коротше          
    if len(monday_list) >=1:
        dict_birthdays["Monday"] = ", ".join(monday_list)
        
    if len(thuesday_list) >=1:
        dict_birthdays["Thuesday"] = ", ".join(thuesday_list)
    
    if len(wednesday_list) >=1:
        dict_birthdays['Wednesdey'] = ", ".join(wednesday_list)
        
    if len(thursday_list) >=1:
        dict_birthdays['Thursday'] = ", ".join(thursday_list)
        
    if len(friday_list) >=1:
        dict_birthdays['Friday'] = ", ".join(friday_list)
    
    for day, bir in dict_birthdays.items():
        print(f"{day} : {bir}")
        
    print (dict_birthdays)
                
    # print(f"{monday_list}\n{thuesday_list}\n{wednesday_list}\n{thursday_list}\n{friday_list}")
            
            



#//How to add value to dictionary in python?
 
birthday(users)
