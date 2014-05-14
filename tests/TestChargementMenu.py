from nose.tools import *
from foodOverview.Menu import Menu


def testChargementMenuSimple():
    fichierMenu = givenUnMenuSimple()
    menu = whenLeMenuEstCharge(fichierMenu)

    thenLeMenuContient('crepe salee', menu)
    thenLeMenuContient('sandwich', menu)
    thenLeMenuContient('canette', menu)

    thenLeProduitCoute('sandwich', 3, menu)
    thenLeProduitCoute('crepe salee', 1.5, menu)

def givenUnMenuSimple():
    return './tests/ressources/menu_simple.yml'

def whenLeMenuEstCharge(fichierMenu):
    return Menu(fichierMenu)

def thenLeMenuContient(produit, menu):
    print menu.getProducts()
    assert_true(menu.findProduct(produit) != None)

def thenLeProduitCoute(produit, prix, menu):
    assert_equal(menu.findProduct(produit).getPrix(), prix)
