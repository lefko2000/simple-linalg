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
        out = [list(i) for i in zip(*self)]
        return out
        
    def prod(self, mat):
        pass
        out = Matrix()
        for i in self:
            vecTemp = Vector()
            for j in mat:
                vecTemp.append(i.scalProd(j))
            out.append(vecTemp)
        return out
    
if __name__ == '__main__':
    a = Matrix([Vector([1,1]), Vector([2,2])])
    b = Matrix([Vector([1,1]), Vector([1,1])])
    print a.prod(b)          
    
            
            
        
        