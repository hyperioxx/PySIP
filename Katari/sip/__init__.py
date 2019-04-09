from .utils import Message

class SipMessage(Message):
    def __init__(self,message=None):
        super().__init__(message=message)
        self.sip_type = None
        self._payload = None


    def get_to(self):
        try:
            return self._data['to']
        except KeyError:
            return None

    def get_from(self):
        try:
            return self._data['from']
        except KeyError:
            return None

    def get_via(self):
        try:
            return  self._data['via']
        except KeyError:
            return None

    def set_via(self, via):
        self._data['via'] = via

    def set_from(self, from_):
        self._data['from'] = from_

    def set_to(self, to):
        self._data['to'] = to

    def set_contact(self, contact):
        self._data['contact'] = contact

    def set_call_id(self, call_id):
        self._data['call-id'] = call_id

    def set_allow(self, allow):
        self._data['allow'] = allow

    def set_message_type(self, message_type):
        self.sip_type = message_type


    def export(self):
        message = ""
        message = message + self.method_line
        for k,v in self._data.items():
            line = k.capitalize() + ": " + v
            message = message + line + "\r\n"
            print(line)
        message = message + "\r\n"
        return message


    def create_response(self,message=None):
        message.set_via(self._data['via'])
        message.set_from(self._data['from'])
        message.set_to(self._data['to'])
        message.set_contact(self._data['contact'])
        message.set_call_id(self._data['call-id'])
        return message



