#!/usr/bin/python3

""" Square that defines a square by:
(based on 1-square.py) """

class Square:
   
    """ Defining the class Square """
  
    def __init__(self, size=0):
        """ Initializing a the class """

        if not isinstance(self, int):
            raise TypeError("size must be an integer") 
        elif size < 0:
            raise ValueError("size must be >= 0 ")
        self._size = size
    
