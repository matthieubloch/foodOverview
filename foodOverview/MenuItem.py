# -*- encoding: utf-8 -*-

class MenuItem(object):
    name = "inconnu"
    price = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def fromNameAndPrice(name, price):
        return MenuItem(name, price)

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def __str__(self):
        return "produit {0}: {1} euro".format(self.name, self.price)

    def __repr__(self):
        return self.__str__()
