import unittest
import cubeVolume

class testCase(unittest.TestCase):
	def test1(self):
		self.assertEqual(cubeVolume.getVolume(2,2,2,),8)
	def test2(self):
		self.assertEqual(cubeVolume.getVolume(2,2,-2),8)
	def test3(self):
		self.assertEqual(cubeVolume.getVolume(0,1,1),None)

if __name__ == '__main__':
	unittest.main()