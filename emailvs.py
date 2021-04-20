import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("ridhamdiyora7@gmail.com","Ridham@07")
server.sendmail("ridhamdiyora7@gmail.com","ridhamdiyora7@gmail.com","hey Ridham Diyora")
server.quit()