import unittest
from chapter_11_3 import Employee

class TestCaseEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('a','b')

    def testemployee(self):
        self.assertEqual(100,self.employee.give_raise(100))

    def testemployee2(self):
        self.assertEqual(5000,self.employee.give_raise())

    def testemployee3(self):
        self.assertEqual(5000,self.employee.give_raise(0))

unittest.main()

