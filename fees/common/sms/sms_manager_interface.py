class SmsManagerInterface:

    def __init__(self, sms_sender_title):
        self.sms_sender_title = sms_sender_title

    def send_sms(self, phone_number, content):
        pass
