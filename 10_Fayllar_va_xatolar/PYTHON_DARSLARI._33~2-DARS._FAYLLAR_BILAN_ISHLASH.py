# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:49:07 2022

@author: Ogabek
"""
#from info import pickle

import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':'2003', 'kurs':2}
talaba2 = {'ism':'ali', 'familiya':'husanov', 'tyil':'2000', 'kurs':1}

with open('info','wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)