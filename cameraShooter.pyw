import smtplib,ssl,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import requests,cv2,os

class System:

    ## Set those information according to your informations.
    sender_mail = "your_sender_mail@gmail.com"
    sender_mail_password = "yousender_mail_password"
    receiver_mail = "your_receiver_email@gmail.com"
    ##########
    
    
    time = str(datetime.datetime.now().replace(microsecond=0))
    context = ssl.create_default_context()
    text = f"Your Computer is Opened! {time}"
    img_path = f'C:/Users/{os.environ["USERNAME"]}/QWERTY.png'
    def connect(self,google_url="https://www.google.com/"):
        try:
            requests.get(google_url)
            return True
        except:
            return False
    def capture_webcam_photo(self):
        cap =  cv2.VideoCapture(0)
        ret,frame = cap.read()
        cv2.imwrite(self.img_path,frame)
    def send_email(self):
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=self.context) as server:
            messages  = MIMEMultipart()
            messages['From'] = self.sender_mail
            messages['To'] = self.receiver_mail
            messages['Subject'] = self.text
            messages.attach(MIMEText(self.text,"plain"))
            with open(self.img_path,"rb") as attachment:
                part =  MIMEBase("application","octet-stream")
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header("Content-Disposition",
            f'attachment; filename={self.img_path}')

            messages.attach(part)
            message_strings = messages.as_string()

            server.login(self.sender_mail,self.sender_mail_password)
            server.sendmail(self.sender_mail,self.receiver_mail,message_strings)



system = System()
system.capture_webcam_photo()
while not system.connect():
    time.sleep(5)
system.send_email()
