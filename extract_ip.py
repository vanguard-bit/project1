import subprocess as subp
import send_mail as sendmail
import pprint as pprint


def extract(Severity):
    val = subp.getstatusoutput('ipconfig')
    if val[0] == 0:
        data = val[1].split('\n')
        data = '\n'.join(data)
        sendmail.send(val[1], Severity)
        return 0
    else:
        return 1


if __name__ == "__main__":
    extract()
