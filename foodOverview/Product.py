# -*- coding: utf-8 -*-
from MenuItem import MenuItem

class Product (MenuItem):
    def __init__(self, name, price):
        super(Product, self).__init__(name, price)


