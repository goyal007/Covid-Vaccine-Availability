import smtplib
from email.message import EmailMessage

def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['to']= to
    
    user = "sender@gmail.com"
    msg['from']=user
    # go to https://myaccount.google.com/
    #Go to security tab
    #setup the 2 step verification and get the app password from there
    password = "abcdefghijklmnop" #app password
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()
    
import requests
from datetime import date
headers = {
    'accept': 'application/json',
    'Accept-Language': 'hi_IN',
    'User-Agent': '', # Enter User-Agent from the network tab after clicking inspect element on the URL page
}
params = (
    ('pincode', '#######'),
    ('date', date.today().strftime('%d-%m-%Y')),
)

import time
c=0
while(1):
    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin', headers=headers, params=params)
    a=response.json()
    for i in range(len(a['centers'])):
        t1 = a['centers'][i]['sessions'][0]['available_capacity']
        t2 = a['centers'][i]['sessions'][0]['min_age_limit']
        t3 = a['centers'][i]['sessions'][0]['date']
        t4 = a['centers'][i]['pincode']
        address = a['centers'][i]['address']
        name_vac = a['centers'][i]['sessions'][0]['vaccine']
        '''print("Pincode:",t4)
        print("available_capacity: ",t1)
        print("min_age_limit: ",t2)
        print("date: ",t3)
        print('\n\n')'''
        if(t1 > 0 and t2 == 18):
            body = str(t1)+" "+name_vac+" vaccine available at "+ address+ " for "+str(t2)+"+" 
            email_alert("Vaccine Availability",body,"receiver@gmail.com")
            print("sent")
    print(c,end=" ")
    
    c+=1
    #fetch information every 60 seconds
    time.sleep(60)
