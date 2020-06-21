class Card:
    def __init__(self, temp):
        self.value = temp

    def getValue(self):
        return self.value


    def filename(self):
        return str(self.value) + ".gif"


