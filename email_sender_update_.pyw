import smtplib,ssl,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import requests,cv2,os,time

class System:
    sender_mail             = "SENDER_MAIL@GMAIL.COM"
    sender_mail_password    = "SENDER_MAIL_PASSWORD"
    receiver_mail           = "RECEIVER_MAIL@GMAIL.COM"
    time        = str(datetime.datetime.now().replace(microsecond=0))
    context     = ssl.create_default_context()
    text        = f"Your Computer is Opened! {time}"
    text_NOCV   = f"Your Computer is Opened! [NOCV] {time}"
    img_path    = f'C:/Users/{os.environ["USERNAME"]}/QWERTY.png'
    def connect(self,google_url="https://www.google.com/"):
        try:
            requests.get(google_url)
            return True
        except:
            return False
    def capture_webcam_photo(self):
        cap =  cv2.VideoCapture(0)
        ret,frame = cap.read()
        if ( ret ):
            cv2.imwrite(self.img_path,frame)
            return True
        return False
    def send_email(self , isCameraActivated ):
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=self.context) as server:
            messages  = MIMEMultipart()
            messages['From'] = self.sender_mail
            messages['To'] = self.receiver_mail
            
            
            if ( isCameraActivated ):
                messages['Subject'] = self.text
                messages.attach(MIMEText(self.text,"plain"))
                with open(self.img_path,"rb") as attachment:
                    part =  MIMEBase("application","octet-stream")
                    part.set_payload(attachment.read())
                
                encoders.encode_base64(part)
                part.add_header("Content-Disposition",
                f'attachment; filename={self.img_path}')
                messages.attach(part)
            else:
                messages['Subject'] = self.text_NOCV
                messages.attach(MIMEText(self.text_NOCV,"plain"))
            message_strings = messages.as_string()

            server.login(self.sender_mail,self.sender_mail_password)
            server.sendmail(self.sender_mail,self.receiver_mail,message_strings)

    def cameraRetry( self ):
        for i in range( 2 ): # 2 times will be tried..
            if ( not self.capture_webcam_photo() ):
                time.sleep(5)
            else:
                return True
        return False

    def handler( self ):
        for i in range( 60 ): # 5 min  try 5-sec intervals.
            if ( not self.connect() ):
                time.sleep(5)
            else:
                CV_STATUS = self.cameraRetry()
                self.send_email( CV_STATUS )
                exit(0)
        

                

SYSTEM = System()
SYSTEM.handler()
