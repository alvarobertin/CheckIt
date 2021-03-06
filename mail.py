import smtplib, ssl

def send():
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    keys = open("keys.private", "r")
    lines = keys.readlines()
    sender_email, password, receiver_email = lines[0].strip().split()
    message = """\
    Subject: NEW PC IN STOCK

    NEW PC IN STOCK: https://www.falabella.com.co/falabella-co/category/cat4920940/Computadores-Gaming """

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
            server = smtplib.SMTP("smtp.gmail.com")
            server.connect(smtp_server, port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()