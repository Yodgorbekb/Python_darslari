# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:25:22 2022

@author: Ogabek
"""

import unittest
from Python_darslari_37dars_AMALIYOT import Shaxs

class PyTest(unittest.TestCase):
    """Klassni tekshiruvchi klass"""
    def setUp(self):
        ism = "Alijon"
        familiya = "Valiyev"
        passport = "P5N6M7"
        tyil = 2000
        self.odam1 = Shaxs(ism,familiya,passport,tyil)
        self.odam2 = Shaxs(ism,familiya,passport,tyil)
        
    def test_create(self):
        #Qiymatlar mavjudligini tekshiramiz
        self.assertIsNotNone(self.odam1.ism)
        self.assertIsNotNone(self.odam1.familiya)
        self.assertIsNotNone(self.odam1.passport)
        self.assertIsNotNone(self.odam1.tyil)
        

unittest.main()