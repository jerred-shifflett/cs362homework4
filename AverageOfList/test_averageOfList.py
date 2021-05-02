import unittest
import averageOfList

list1= [10.0,15.0,20.0,25.0,30.0,35.0]
list2 = []
list3 = [10,2,4,-4]

class testCase(unittest.TestCase):
	
	def test1(self):
		self.assertEqual(averageOfList.Average(list1),22.5)
	def test2(self):
		self.assertEqual(averageOfList.Average(list2),1)
	def test3(self):
		self.assertEqual(averageOfList.Average(list3),3.0)

if __name__ == '__main__':
	unittest.main()