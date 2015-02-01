# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 11:41:18 2015

@author: Admin
"""

from linalg import  Vector, Matrix
import unittest

class TestVector(unittest.TestCase):
    
    def test_vec_mult(self):
        a = Vector([1,1])
        b = Vector([2,2])
        c = Vector([2,2])
        self.assertEqual(a.mult(b),c)
        
class TestMat(unittest.TestCase):
    
    def test_Transpose(self):
        a = Matrix( [Vector([1,2]) , Vector([3,4])] )
        b = Matrix( [Vector([1,3]), Vector([2,4])] )
        self.assertEqual(a.T(), b)
        
if __name__ == '__main__':
    unittest.main()