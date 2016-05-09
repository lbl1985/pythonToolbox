import unittest, os, sys, re

class TestStringMethods(unittest.TestCase):
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_intvet_no_arguments(self):
		os.system("c:/work/intvet/intvet.exe > c:/work/intvet/output.txt")
		reg = re.compile('IntVet Common Options')
		fp = open ('c:/work/intvet/output.txt', 'r')
		str = fp.read()
		self.assertRegexpMatches(str, reg)

if __name__ == '__main__':
	unittest.main()