# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:06:40 2022

@author: Ogabek
"""

import unittest

from cars import Car

class CarTest(unittest.TestCase):
    """Car klassini tekshiradigan klass"""
    def setUp(self):
        make = "GM"
        model = "Malibu"
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make, model, year)
        self.avto2 = Car(make, model, year,price=self.price)

    def test_create(self):
        #Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiradi
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        #Qiymat mavjud emasligini assertIsNone metodi bilan tekshiradi
        self.assertIsNone(self.avto1.price)
        #Qiymat tengligini assertEqual metodi bilan tekshiradi
        self.assertEqual(0,self.avto1.get_km())
        # avto2 narhini tekshiramiz
        self.assertEqual(self.price,self.avto2.price)
        
    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price,self.avto2.price)
        
    def test_add_km(self):
        #1 Musbat qiymat berib ko'ramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km())
        self.avto1.add_km(5000)
        self.assertEqual(15000,self.avto1.get_km())
        #2 Manfiy qiymat berib tekshirib ko'ramiz
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
        
unittest.main()