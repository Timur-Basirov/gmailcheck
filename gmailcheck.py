#    # ckxx xldu jcgf ugol 
# import smtplib, ssl
# from email.message import EmailMessage
# smtp_server="smtp.gmail.com"
# port=587 #For starttls
# sender_email="atimur.basirov@gmail.com"
# # to_email="atimur.basirov@gmail.com"
# password=input("Type your password and press enter: ")
# #Create a secure SSL context
# context=ssl.create_default_context()
# msg= EmailMessage()
# msg.set_content("Congratulations")
# msg['Subject']="S 8 marta"
# msg['From']="atimur.basirov@gmail.com"#Try to log in to server and send email
# msg['To']="marina.oleinik@tthk.ee"
# try:
#     server=smtplib.SMTP(smtp_server,port)
#     server.ehlo() #Can be omitted
#     server.starttls(context=context) #Secure the connection
#     server.ehlo() #Can be omitted
#     server.login(sender_email, password)
#     # server.sendmail(sender_email,to_email,msg)
#     server.send_message(msg)
# except Exception as e:
#     #Print any error mesages to stdout
#     print(e)
# finally:
#     server.quit
    
