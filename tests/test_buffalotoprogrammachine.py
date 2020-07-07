import unittest

from buffalotoprogrammachine import reverse_binary_to_decimal, buf_list_to_binary

class Test_Reverse_Binary_To_Decimal(unittest.TestCase):
    def test(self):
            self.assertEqual(reverse_binary_to_decimal(list('0')), 0)
            self.assertEqual(reverse_binary_to_decimal(list('1')), 1)
            self.assertEqual(reverse_binary_to_decimal(list('01')), 2)
            self.assertEqual(reverse_binary_to_decimal(list('110')), 3)
            self.assertEqual(reverse_binary_to_decimal(list('001')), 4)
            self.assertEqual(reverse_binary_to_decimal(list('101')), 5)
            self.assertEqual(reverse_binary_to_decimal(list('101000000')), 5)
        
class Test_Buf_List_To_Binary(unittest.TestCase):
    def test(self):
        self.assertEqual(buf_list_to_binary('buffalo buffalo'.split()), 0)
        self.assertEqual(buf_list_to_binary('Buffalo buffalo'.split()), 1)
        self.assertEqual(buf_list_to_binary('buffalo buffalo Buffalo buffalo'.split()), 2)
        self.assertEqual(buf_list_to_binary('Buffalo buffalo Buffalo buffalo'.split()), 3)