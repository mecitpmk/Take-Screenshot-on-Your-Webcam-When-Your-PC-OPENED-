# Send Email When Your PC Opened
When your computer is opened, software automatically run if you do those steps:

### IMPORTANT UPDATE!
Because of the Google privacy issues, you have to activate 2-step verification process for sender e-mail. link in below. <br />
https://exerror.com/smtplib-smtpauthenticationerror-username-and-password-not-accepted/ <br/>

### First way:
1- press WindowsLogo+R and type shell:startup<br />
2- paste this pyw file into this folder. (Dont forget to change sender,receiver mail)<br />

### Second way:
Go to below  path (Change USERNAME keyword into your PC current USERNAME)<br />
1- C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup<br />
2- paste this pyw file into this folder. (Dont forget to change sender,receiver mail)<br />

## Attention Before Using
Open file in edit mode and change those variables to the your current mail adress.
### -> sender_mail = "your_sender_mail@gmail.com"
### -> sender_mail_password = "yousender_mail_password"
### -> receiver_mail = "your_receiver_email@gmail.com"


## When Your Computer is Opened
This software first of all, check your internet connection. If its stable, try to send it.
If your connection is not available, this software check your connection for every 5 sec. And when its available software will send it.
![automail](https://user-images.githubusercontent.com/63451008/107440414-a11e5580-6b44-11eb-8657-5df405566d10.PNG)


## License
MIT Licance
