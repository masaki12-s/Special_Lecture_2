import unittest
# import os,sys
# sys.path.append(os.path.join("..","speciallecture"))
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read1(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))
        # self.assertRaises()
    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        print(l)
    def test_read3(self):
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter("sample2.csv")
            l = printer.read()
