from .utils.langageInterface import langageInterface

class Ohce:

    def __init__(self, langage=None):
        self.expressions = langageInterface(langage).sentences
        self.greet()

    def __del__(self):
        self.salute()

    def palindrome(self, string):
        miroir = self.miroir(string)
        print(miroir)
        if (miroir == string):
            print(self.congrate())

    def miroir(self, string):
        return string[::-1]

    def salute(self):
        return self.expressions.salute

    def greet(self):
        return self.expressions.greet

    def congrate(self):
        return self.expressions.congrate
