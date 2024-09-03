# import smtplib as smtplib


def send(Data, Severity):
    file_name = open("Alert.txt", "w")
    message = Data + '\n\n' + "Severity level is " + str(Severity)
    file_name.write(message)
    file_name.close()
    # port = 567
    #
    # sender = smtplib.SMTP()
    # sender.connect(stmp_server, port=port)
    # sender.starttls()
    #
    # sender.login(sender_email_id, sender_password)
    # message = Data
    #
    # sender.sendmail(sender_email_id, destination, message)
    # sender.quit()


if __name__ == "__main__":
    send("Severity", 1000)
