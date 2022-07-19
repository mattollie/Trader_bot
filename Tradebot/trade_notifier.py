import smtplib, ssl


def send_email(ticker):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "mhincorporated20@gmail.com"
    receiver_email = "mhincorporated20@gmail.com"
    password = input("Type your password and press enter:")
    message = "You should look at " + str(ticker)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def main(ticker):
    send_email(ticker)


if __name__ == '__main__':
    main()