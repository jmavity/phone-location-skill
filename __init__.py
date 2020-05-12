from mycroft import MycroftSkill, intent_file_handler


class PhoneLocation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('location.phone.intent')
    def handle_location_phone(self, message):
        area_code = message.data.get('area_code')
        exchange = message.data.get('exchange')
        area = ''
        region = ''

        self.speak_dialog('location.phone', data={
            'area': area,
            'area_code': area_code,
            'region': region,
            'exchange': exchange
        })


def create_skill():
    return PhoneLocation()

