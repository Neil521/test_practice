import unittest2 as unittest
from selenium import webdriver
from time import sleep

class Mydemo(unittest.TestCase):
    def setUp(self):
        print('1')
    def Mytest1(self):
        print ("i am Mytest1 the value of a is {}")
    def Mytest2(self):
        print ("i am Mytest2 the value of a is {}")
    def Mytest3(self):
        print ("i am Mytest3 the value of a is {}")
    def tearDown(self):
        print('2')

if __name__ == '__main__':
    unittest.main()
    #runner=unittest.TextTestRunner()
    #test_suit=unittest.TestSuite()
    #test_suit.addTests(map(Mydemo,['Mytest1','Mytest2','Mytest3']))
    #runner.run(test_suit)
