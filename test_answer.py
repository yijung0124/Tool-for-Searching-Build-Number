import unittest
import Test


class TestResult(unittest.TestCase):

	def test_output(self):
		Result1 = Test.output('610240' ,'3.6.2')
		Result2 = Test.output('624890' ,'3.6.2')
		Result3 = Test.output('617485' ,'3.6.2')
		Result4 = Test.output('624021' ,'3.6.2')
		Result5 = Test.output('622893' ,'3.6.2')


		self.assertEqual(Result1, 'http://jenkins-tdc.video54.local:8080/view/ESPP/view/3.6.2/job/R3_6_2_AUTO_BUILD_ALL_IMAGES/42/console')
		self.assertEqual(Result2, 'http://jenkins-tdc.video54.local:8080/view/ESPP/view/3.6.2/job/R3_6_2_AUTO_BUILD_ALL_IMAGES/65/console')
		self.assertEqual(Result3, 'http://jenkins-tdc.video54.local:8080/view/ESPP/view/3.6.2/job/R3_6_2_AUTO_BUILD_ALL_IMAGES/52/console')
		self.assertEqual(Result4, 'http://jenkins-tdc.video54.local:8080/view/ESPP/view/3.6.2/job/R3_6_2_AUTO_BUILD_ALL_IMAGES/63/console')
		self.assertEqual(Result5, 'http://jenkins-tdc.video54.local:8080/view/ESPP/view/3.6.2/job/R3_6_2_AUTO_BUILD_ALL_IMAGES/59/console')



		
if __name__ == '__main__':
	unittest.main()
