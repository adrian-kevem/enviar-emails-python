#!/usr/bin/env python

import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Hello World</p>
    """
    msg = email.message.Message()
    msg['Subject'] = 'Assunto'
    msg['From'] = 'adrianveven@gmail.com'
    msg['To'] = 'adrianveven@gmail.com'
    password = 'irag mvce xrzg kmvk' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email) 
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()