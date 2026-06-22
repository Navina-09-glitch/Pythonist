import sys
class MulTable:
    def getN(self):
        try:
            self.n = int(input("Enter the integer value:"))
        except ValueError: