# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 11:41:18 2015

@author: Admin
"""

from linalg import  Vector
import unittest

class TestVector(unittest.TestCase):
    
    def test_vec_mult(self):
        a = Vector([1,1])
        b = Vector([2,2])
        c = Vector([2,2])
        self.assertEqual(a.mult(b),c)
        
if __name__ == '__main__':
    unittest.main()