#!/usr/bin/python3
import myFunction
import unittest

class Testmultiplyimperfect(unittest.TestCase):

    def test_with_two_pos(self):
        self.assertEqual(myFunction.multiply_with_loop_imperfect(17, 13), 17 * 13)
        self.assertEqual(myFunction.multiply_with_loop_imperfect(123456, 278987), 123456 * 278987)
        self.assertEqual(myFunction.multiply_with_loop_imperfect(1, 2), 2)
    
    def test_with_one_zero(self):
        self.assertEqual(myFunction.multiply_with_loop_imperfect(17, 0), 0)
        self.assertEqual(myFunction.multiply_with_loop_imperfect(0, 17), 0)

    def test_with_two_zeros(self):
        self.assertEqual(myFunction.multiply_with_loop_imperfect(0, 0), 0)

    def test_with_one_neg(self):
        self.assertEqual(myFunction.multiply_with_loop_imperfect(17, -13), 17 * (-13))
        self.assertEqual(myFunction.multiply_with_loop_imperfect(-13, 17), (-13) * 17)

    def test_with_two_negs(self):
        self.assertEqual(myFunction.multiply_with_loop_imperfect(-17, -13), 17 * 13)

class Testmultiplybetter(unittest.TestCase):

    def test_with_two_pos(self):
        self.assertEqual(myFunction.multiply_with_loop_better(17, 13), 17 * 13)
        self.assertEqual(myFunction.multiply_with_loop_better(123456, 278987), 123456 * 278987)
        self.assertEqual(myFunction.multiply_with_loop_better(1, 2), 2)
    
    def test_with_one_zero(self):
        self.assertEqual(myFunction.multiply_with_loop_better(17, 0), 0)
        self.assertEqual(myFunction.multiply_with_loop_better(0, 17), 0)

    def test_with_two_zeros(self):
        self.assertEqual(myFunction.multiply_with_loop_better(0, 0), 0)

    def test_with_one_neg(self):
        self.assertEqual(myFunction.multiply_with_loop_better(17, -13), 17 * (-13))
        self.assertEqual(myFunction.multiply_with_loop_better(-13, 17), (-13) * 17)

    def test_with_two_negs(self):
        self.assertEqual(myFunction.multiply_with_loop_better(-17, -13), 17 * 13)
    