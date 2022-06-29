from django.core.mail import send_mail
import time

send_mail()


class sendEmail():
    def __init__(self, rece_addr, sub_info, cont_info):
        sub_data = time.strftime("%fY-%m-%d_%H:%M:%S", time.localtime())
        self.rece_adde = rece_addr
        self.sub_info = sub_info + sub_data
        self.cont_info = cont_info

    def send(self):
        try:
            send_mail(
                subject=self.sub_info,
                message=self.cont_info,
                from_email="40716@sohu.com",
                recipient_list=self.rece_adde
            )
            return True
        except Exception as e:
            print(e)
            return False
