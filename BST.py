# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:07:38 2019

@author: MOHAN
"""

class Node:
    
    def __init__(self,data):
        
        self.left = None
        self.right =None
        self.data = data
        
        
class Tree:
    
    def __init__(self):
        Tree.root = None

    def insert(self,data):
        new_node = Node(data)
        temp = Tree.root
        print(temp)
        if Tree.root == None:
            Tree.root = new_node
            
        else:
            while temp:
                if temp.data>new_node.data:
                    if temp.left == None:
                        temp.left = new_node   
                        break
                    else:
                        temp = temp.left
                        
                elif temp.data<new_node.data:
                    if temp.right == None:
                        temp.right = new_node 
                        break
                    else:
                        temp = temp.right
                        
    def printer(self,root):
        
        if root:
            bst.printer(root.left)
            print(root.data)
            bst.printer(root.right)
        

        
        
        
if __name__ == '__main__':
    
    bst = Tree()
    while True:
        a = int(input("1.insert\n2.printer"))
        if a == 1:
            bst.insert(int(input("enter the node value")))
        if a == 2:
            bst.printer(Tree.root)
        
                    
            
            