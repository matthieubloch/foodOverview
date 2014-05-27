# -*- coding: utf-8 -*-
import yaml
from Menu import *
from MenuItem import MenuItem
from Product import Product

PRODUCT = 'produit'
MENU_SET = 'formule'
PRICE = 'prix'
class MenuLoader:


    def loadMenu(self, filename):
        file = open(filename)
        content = yaml.load(file)
        return Menu(self.parseMenuElements(content))
        file.close()

    def parseMenuElements(self, content):
        items = []
        for element in content:
            if 'produit' in element:
                items.append(self.parseProduit(element))
            elif 'formule' in element:
                self.parseFormule(element)
            else:
                raise Exception('Fichier mal formé : ' + element)
        return items

    def parseProduit(self, element):
        if PRICE not in element:
            raise Exception('Manque prix pour le produit {}'.format(element[PRODUCT]))
        return Product(element[PRODUCT], element[PRICE])

    def parseFormule(self, element):
        pass
