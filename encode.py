class Coder:
    def __init__(self):
        self.alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890wertyuioqasdfghjklzxcvbnm-!"#$%&()*,./:;?@[]^_`{|}~+<=>'
        self.smeshenie = 5
        self.itog = ''

    def encode(self, message):
        self.itog = ''
        for i in message:
            mesto = self.alfavit_EU.find(i)  # Алгоритм для шифрования сообщения на английском
            new_mesto = mesto + self.smeshenie
            if i in self.alfavit_EU:
                self.itog += self.alfavit_EU[new_mesto % len(self.alfavit_EU)]
            else:
                self.itog += i
        return self.itog
