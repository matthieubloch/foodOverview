# -*- coding: utf-8 -*-
import yaml

class Menu:
    
    products = []

    def __init__(self, filename):
        file = open(filename)
        dataMap = yaml.load(file)
        for product in dataMap:

            self.products.append(
                Product(product['produit'],
                        product['prix'])
            )

        file.close()

    def findProduct(self, productName):
        for product in self.products:
            if productName == product.getName():
                return product
        return None

    def getProducts(self):
        return self.products

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def getName(self):
        return self.name

    def getPrix(self):
        return self.price

    def __str__(self):
        return "produit {0}: {1} euro".format(self.name, self.price)
    
    def __repr__(self):
        return self.__str__()
