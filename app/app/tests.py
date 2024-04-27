from django.test import SimpleTestCase

from app import calc

class CalcCheck(SimpleTestCase):
    def test_calc_fun(self):
        res = calc.add(4,5)
        self.assertEqual(res,9)