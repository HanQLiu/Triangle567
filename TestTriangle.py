# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(201, 100, 100),'InvalidInput','201 ,100 ,100 is a Invalid triangle')
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(100, 201, 100), 'InvalidInput', '100, 201, 100 is a Invalid triangle')
    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(100, 100, 201), 'InvalidInput', '100, 100, 201 is a Invalid triangle')
    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', '0, 1, 1 is a Invalid triangle')
    def testInvalidInputE(self):
        self.assertEqual(classifyTriangle(1, 0, 1), 'InvalidInput', '1, 0, 1 is a Invalid triangle')
    def testInvalidInputF(self):
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', '1, 1, 0 is a Invalid triangle')
    def testInvalidInputG(self):
        self.assertEqual(classifyTriangle(0.1, 1, 1), 'InvalidInput', '0.1, 1, 1 is a Invalid triangle')
    def testInvalidInputH(self):
        self.assertEqual(classifyTriangle(1, 'a', 1), 'InvalidInput', '1, "a", 1 is a Invalid triangle')
    def testInvalidInputI(self):
        self.assertEqual(classifyTriangle(1, 1, False), 'InvalidInput', '1, 1, false is a Invalid triangle')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle', '1 ,1 ,2 is a not a triangle')
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 3, 1), 'NotATriangle', '1, 3, 1 is a not a triangle')
    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(4, 2, 2), 'NotATriangle', '4, 2, 2 is a not a triangle')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5),'Right', '3, 4, 5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4),'Right','5, 3, 4 is a Right triangle')
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right', '3, 5, 4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1),'Equilateral','1, 1, 1 should be equilateral')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2, 3, 4 should be scalene')
    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(5, 7, 6), 'Scalene', '5, 7, 6 should be scalene')
    def testScaleneTrianglesC(self):
        self.assertEqual(classifyTriangle(10, 9, 8), 'Scalene', '10, 9, 8 should be scalene')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2, 2, 3 should be Isoceles')
    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(4, 5, 4), 'Isoceles', '4, 5, 4 should be Isoceles')
    def testIsoscelesTrianglesC(self):
        self.assertEqual(classifyTriangle(7, 6, 6), 'Isoceles', '7, 6, 6 should be Isoceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

