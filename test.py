'''
The file is used to add test case for the main function
'''
from main import calTotal

def test_strike():
    s = 'XXXXXXXXXXXX'
    assert calTotal(s) == 300

def test_miss():
    s = '9-9-9-9-9-9-9-9-9-9-'
    assert calTotal(s) == 90

def test_spare():
    s = '5/5/5/5/5/5/5/5/5/5/5'
    assert calTotal(s) == 150

def test_general():
    s = 'X7/9-X-88/-6XXX81'
    assert calTotal(s) == 167