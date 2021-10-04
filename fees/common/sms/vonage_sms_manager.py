import vonage


from fees.common.sms.sms_manager_interface import SmsManagerInterface


class VonageSmsManager(SmsManagerInterface):

    def __init__(self, sms_sender_title, api_key, api_secret):
        super().__init__(sms_sender_title)
        self.client = vonage.Client(key=api_key, secret=api_secret)
        self.sms = vonage.Sms(self.client)

    def send_sms(self, phone_number, content):
        self.sms.send_message({
            'from': self.sms_sender_title,
            'to': str(phone_number)[1:],
            'text': content
        })
