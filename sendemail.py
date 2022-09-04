import smtplib, ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "programador.mirim1@gmail.com"
    password="Thom!0807"
    receiver_email= "ise.pentester@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context) #that it wants to upgrade from an insecure to secure connection using TLS or SSL. SSL context to secure the connection.
        server.login(sender_email, password) #tries to log into that particular id
        server.sendmail(sender_email, receiver_email, message)
        
    except Exception as e:
        print(e)
    finally:
        server.quit()
    
