from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self): 
        self.browser.quit()

    def test(self):

        #โจ้ต้องการลดน้ำหนักและคุมน้ำตาลเขาจึงเขาเข้ามาที่ web "FoodSuger"
        self.browser.get('http://localhost:8000/FoodSuger')
        self.assertIn('FoodSuger', self.browser.title) 
   
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ข้าวผัดหมู', header_text)
        
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('pizza', header_text)
        
        #โจ้จึงได้เห็นระดับน้ำตาลของอาหาร "ข้าวผัดหมู"
        header_suger_text = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('Suger ข้าวผัดหมู', header_suger_text)
        suger_text = self.browser.find_element_by_tag_name('p2').text
        self.assertIn('50%', suger_text)

        #โจ้จึงได้เห็นระดับน้ำตาลของอาหาร "pizza"
        header_suger_text = self.browser.find_element_by_tag_name('p3').text
        self.assertIn('Suger pizza', header_suger_text)
        suger_text = self.browser.find_element_by_tag_name('p4').text
        self.assertIn('80%', suger_text)
        
        
        #โจ้เห็นว่าระดับน้ำตาลของ pizza ที่เขาค้นหานั้นต่ำกว่า web 
        #โจ้จึงได้ลองลบระดับน้ำตาลของ pizza
        inputbox = self.browser.find_element_by_id('delete_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Delete Food')
        inputbox.send_keys('pizza')
        self.browser.find_element_by_id('delete').click()
        

        #เมื่อโจ้กลับมาดูก็พบว่าอาหารที่เขาค้นหานั้นหายไปแล้ว
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ข้าวผัดหมู', header_text)

        header_suger_text = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('suger ข้าวผัดหมู', header_suger_text)

        suger_text = self.browser.find_element_by_tag_name('p2').text
        self.assertIn('70%', suger_text)

        
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertNotIn('pizza', header_text)

        header_suger_text = self.browser.find_element_by_tag_name('p3').text
        self.assertNotIn('suger pizza', header_suger_text)

        suger_text = self.browser.find_element_by_tag_name('p4').text
        self.assertNotIn('80%', suger_text)


        # โจ้จึงได้เพิ่มอาหาร
        inputbox = self.browser.find_element_by_id('new_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your new Food')
        inputbox.send_keys('BBQ')

        inputbox = self.browser.find_element_by_id('new_text_suger')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your new Suger')
        inputbox.send_keys('80%')

        self.browser.find_element_by_id('submit').click()

        #เมื่อโจ้กลับมาดูก็พบว่าระดับน้ำตาลของอาหารที่เขาค้นหานั้นคืนมาแล้ว
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('BBQ', header_text)

        header_suger_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Suger BBQ', header_suger_text)

        suger_text = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('80%', suger_text)

        
        time.sleep(5)
        self.fail('Finish the test!') 


if __name__ == '__main__': 
    unittest.main(warnings='ignore')


        
