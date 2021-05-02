import unittest
import fullFirstLastName
FirstName1 = "Jerred"
LastName1 = " Shifflett"
FirstName2 = "Test"
LastName2= 25
FirstName3= ""
LastName3= ""
class testCase(unittest.TestCase):
	
	def test1(self):
		self.assertEqual(fullFirstLastName.Fullname(FirstName1,LastName1),"Jerred Shifflett")
	def test2(self):
		self.assertEqual(fullFirstLastName.Fullname(FirstName2,LastName2),"Test25")
	def test3(self):
		self.assertEqual(fullFirstLastName.Fullname(FirstName3,LastName3),"")

if __name__ == '__main__':
	unittest.main()