# -*- coding: utf-8 -*-
from MenuItem import MenuItem
from Product import Product

class Menu:

    products = []

    def __init__(self, products):
        self.products = products

    def findProduct(self, productName):
        for product in self.products:
            if productName == product.getName():
                return product
        return None

    def getProducts(self):
        return self.products

    def addItem(self, item):
        self.product.append(item)

    def __str__(self):
        menuStr = ''
        for item in self.products:
            menuStr = "{}{}\n".format(menuStr, item)
        return menuStr

    def __repr(self):
        return self.__str__()
