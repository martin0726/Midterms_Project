from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()

	def test_can_display_ingredients_list(self):


		self.browser.get('http://localhost:8000/ingredients_list')


		self.assertIn('Ingredients - List', self.browser.title)
		

		self.assertIn(self.browser.current_url,
			'http://localhost:8000/ingredients_list')
	
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')