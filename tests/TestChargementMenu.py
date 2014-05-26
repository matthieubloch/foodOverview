from nose.tools import *
from foodOverview.Menu import Menu

ressources = './tests/ressources/'
menu_simple = 'menu_simple.yml'
menu_complexe = 'menu_complexe.yml'

fichierMenu = ''
menu = ''

def testChargementMenuSimple():
    givenUnMenuSimple()
    menu = whenLeMenuEstCharge()

    thenLeMenuContient('crepe salee')
    thenLeMenuContient('sandwich')
    thenLeMenuContient('canette')

    thenLeProduitCoute('sandwich', 3)
    thenLeProduitCoute('crepe salee', 1.5)

def testChargementProduitComposite():
    givenUnMenuComplexe()

def givenUnMenuSimple():
    global fichierMenu
    fichierMenu = ressources + menu_simple

def givenUnMenuComplexe():
    global fichierMenu
    fichierMenu = ressources + menu_complexe

def whenLeMenuEstCharge():
    global menu
    menu = Menu(fichierMenu)

def thenLeMenuContient(produit):
    assert_true(menu.findProduct(produit) != None)

def thenLeProduitCoute(produit, prix):
    assert_equal(menu.findProduct(produit).getPrix(), prix)
