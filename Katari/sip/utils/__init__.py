from collections import OrderedDict

class Message:

    def __init__(self, message):
        self.raw_message = message
        self.method_line, self.headers = message.decode().split('\r\n', 1)
        self._data = OrderedDict()
        self._parser(self.headers)
        self.sip_type = self.get_method(self.method_line)


    def __getitem__(self, item):
        try:
            return self._data[item]
        except KeyError:
            return None


    def _parser(self, message):
         for line in message.split("\r\n"):
             try:
                  header, data = line.split(": ")
                  self._data[header.lower()] = data
             except Exception as e:
                 pass

    def get_method(self, methodline):
        return methodline.split()[0]




class URI:
    def __init__(self,uri):
        pass


class AllowType:
    def __init__(self):
        pass