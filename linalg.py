# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 12:11:25 2015

@author: Admin
"""

class Vector(list):
    def __init__(self, data = []):
        for i in data:
            self.append(i)
    
    def add(self, other):
        
        out = []
        for i, j in zip(self, other):
            out.append(i+j)
        return out
        
    def neg(self):
        out = []
        for i in self.data:
            out.append(-i)
        return out
        
    def mult(self, other):
        out = []
        for i, j in zip(self, other):
            out.append(i*j)
        return out
        
    def sub(self, other):
        return self.add(other.neg())
        
    def scalProd(self, other):
        return sum(i*j for i,j in zip(self,other))
        
        
            

class Matrix(list):
    
    def __init__(self, vecList = []):
        for i in vecList:
            self.append(i)
    
    def nrow(self):
        return len(self)
        
    def ncol(self):
        return len(self[0])
                
    def add(self, mat):
        out = []
        for i, j in zip(self, mat):
            out.append(i.add(j))
        return out
        
    def T(self):
        r = self.nrow()
        c = self.ncol()
        out = Matrix()
        for i in range(c):
            vecTemp = Vector()
            for j in range(r):
                vecTemp.append(self[j][i])
            out.append(vecTemp)
        return out        
        
    def mult(self, mat):
        pass
        out = Matrix()
        r = self.nrow()
        c = mat.ncol()
        for i in range(r):
            vecTemp = Vector()
            for j in range(c):
                vecTemp
    
if __name__ == '__main__':
    a = Matrix([Vector([1,2]), Vector([3,4])])
    print a
    print a.T()
    print Vector([1,2]).add(Vector([3,4]))
    print Vector([1,2])
                
    
            
            
        
        