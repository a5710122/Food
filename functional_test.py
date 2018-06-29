from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self): 
        self.browser.quit()

    def test(self):

        #โจ้ต้องการลดน้ำหนักและคุมน้ำตาลเขาจึงเขาเข้ามาที่ web "Food"
        self.browser.get('http://localhost:8000/fooddetail')
        self.assertIn('FoodDetail', self.browser.title) 
   
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ข้าวผัดหมู', header_text)
        
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('pizza', header_text)
        
        #โจ้จึงได้เห็นระดับน้ำตาลของอาหาร "ข้าวผัดหมู"
        header_sugar_text = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('Sugar ข้าวผัดหมู', header_sugar_text)
        sugar_text = self.browser.find_element_by_tag_name('p2').text
        self.assertIn('50%', sugar_text)

        #โจ้จึงได้เห็นระดับน้ำตาลของอาหาร "pizza"
        header_sugar_text = self.browser.find_element_by_tag_name('p3').text
        self.assertIn('Sugar pizza', header_sugar_text)
        sugar_text = self.browser.find_element_by_tag_name('p4').text
        self.assertIn('80%', sugar_text)
        
        
        #โจ้เห็นว่าระดับน้ำตาลของ pizza ที่เขาค้นหานั้นต่ำกว่า web 
        #โจ้จึงได้ลองลบระดับน้ำตาลของ pizza
        inputbox = self.browser.find_element_by_id('delete_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Delete Food')
        inputbox.send_keys('pizza')
        self.browser.find_element_by_id('delete').click()
        

        #เมื่อโจ้กลับมาดูก็พบว่าอาหารที่เขาค้นหานั้นหายไปแล้ว
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ข้าวผัดหมู', header_text)

        header_sugar_text = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('sugar ข้าวผัดหมู', header_sugar_text)

        sugar_text = self.browser.find_element_by_tag_name('p2').text
        self.assertIn('70%', sugar_text)

        
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertNotIn('pizza', header_text)

        header_sugar_text = self.browser.find_element_by_tag_name('p3').text
        self.assertNotIn('sugar pizza', header_sugar_text)

        sugar_text = self.browser.find_element_by_tag_name('p4').text
        self.assertNotIn('80%', sugar_text)


        # โจ้จึงได้เพิ่มอาหาร
        inputbox = self.browser.find_element_by_id('new_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your new Food')
        inputbox.send_keys('BBQ')

        inputbox = self.browser.find_element_by_id('new_text_sugar')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your new Sugar')
        inputbox.send_keys('80%')

        self.browser.find_element_by_id('submit').click()

        #เมื่อโจ้กลับมาดูก็พบว่าระดับน้ำตาลของอาหารที่เขาค้นหานั้นคืนมาแล้ว
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('BBQ', header_text)

        header_sugar_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Sugar BBQ', header_sugar_text)

        sugar_text = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('80%', sugar_text)

        
        time.sleep(5)
        self.fail('Finish the test!') 


if __name__ == '__main__': 
    unittest.main(warnings='ignore')


        
