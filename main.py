import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas
import csv
from sys import *
import os

def data(file_name):

    birthday_data=list
    path=os.path.abspath(file_name)
    is_file=os.path.isfile(path)
    day = datetime.datetime.now().day
    month=date = datetime.datetime.now().month
    todays_date=(day,month)
    birthday_person_data=[]

    
    if is_file==True:
        with open(path,mode="r") as csv_file:
            data=pandas.read_csv(csv_file)

        for (index, data_row) in data.iterrows():
            birth_data={(data_row["Day"],data_row["Month"]):(data_row["First Name"],data_row["Last name"],data_row["Email_id"])}

            if todays_date in birth_data.keys():
                d=birth_data[todays_date]
                birthday_person_data.append(d)

    return (birthday_person_data)

def send_mail(file_name):
   
    user_data=data(file_name)


    for each in user_data:
        fromaddr = "{your mail id}"
        to_add=each[2]


        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = to_add

        # storing the subject
        msg['Subject'] = "HAPPY BIRTHDAY 🎂 "

        # string to store the body of the mail
        body = f"Hi {each[0]},\njust wanted to drop you a quick line to wish you a very happy birthday!\n" \
               f"I hope you have a great day.\n-{your name}"

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent

        filename = f"birthday.jpg"
        abs_path = os.path.abspath('birthday.jpg')

        attachment = open(abs_path, "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication

        s.login(fromaddr, os.getenv("password")) #store yoour password in environment variable named as password"

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, to_add, text)

        # terminating the session
        s.quit()

def main():
    send_mail("Birthdays.csv")
if __name__=="__main__":
    main()
