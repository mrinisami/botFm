class Message:


    def __init__(self, message):
        self.raw = message
        self.loc = 0
        self._readShort()



    def _readShort(self):
        value = eval("0x" + self.raw[self.loc:self.loc + 4])
        print(value)
        self.loc += 4
        return value



