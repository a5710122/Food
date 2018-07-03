from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time


class NewVisitorTest(LiveServerTestCase):

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self): 
        self.browser.quit()


    def test(self):

        #โจ้ต้องการลดน้ำหนักและคุมน้ำตาลเขาจึงเขาเข้ามาที่ web "Food"
        self.browser.get(self.live_server_url)
        self.assertIn('Home Food', self.browser.title) 
        header_food_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome to HomePage Food', header_food_text)
        self.browser.find_element_by_id('to_page_fooddetail').click()

        # โจ้จึงได้เพิ่มอาหาร "ข้าวผัดหมู have sugar: 80 % "
        inputbox = self.browser.find_element_by_id('new_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your new food')
        inputbox.send_keys('ข้าวผัดหมู')

        inputbox = self.browser.find_element_by_id('new_text_sugar')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your sugar')
        inputbox.send_keys('80')

        self.browser.find_element_by_id('submit_new_text_food').click()
        
   
        #เมื่อเขาเข้ามาที่ "Food Detail" โจ้จึงได้เห็นระดับน้ำตาลของอาหาร "ข้าวผัดหมู"
        self.assertIn('FoodDetail', self.browser.title)
        table = self.browser.find_element_by_id('food_table')  
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1. ข้าวผัดหมู have sugar: 80 %', [row.text for row in rows])
        time.sleep(3)

        #โจ้พบว่าเขาใส่ระดับน้ำตาลของ "ข้าวผัดหมู" ผิด เขาจึงเข้าไปแก้ไขระดับน้ำตาลของ "ข้าวผัดหมู" 
        #แต่ว่าโจ้เห็น Delete Food ก่อนเขาจึงตัดสินใจลบ "ข้าวผัดหมู" ทิ้ง
        inputbox = self.browser.find_element_by_id('delete_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Delete Food')
        inputbox.send_keys('ข้าวผัดหมู')
        self.browser.find_element_by_id('submit_delete_text_food').click()
        
        #เมื่อเขาเข้ามาที่ "Food Detail" โจ้จึงได้เห็น "ข้าวผัดหมู" ถูกลบไปแล้ว
        table = self.browser.find_element_by_id('food_table')  
        rows = table.find_elements_by_tag_name('tr')
        self.assertNotIn('1. ข้าวผัดหมู have sugar: 80 %', [row.text for row in rows])
        time.sleep(3)

        # โจ้จึงได้เพิ่ม "ข้าวผัดหมู have sugar:70 % "
        inputbox = self.browser.find_element_by_id('new_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your new food')
        inputbox.send_keys('ข้าวผัดหมู')
        inputbox = self.browser.find_element_by_id('new_text_sugar')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your sugar')
        inputbox.send_keys('70')
        self.browser.find_element_by_id('submit_new_text_food').click()

        #เมื่อเขาเข้ามาที่ "Food Detail" โจ้จึงได้เห็นระดับน้ำตาลของอาหาร "ข้าวผัดหมู"ที่เพิ่มใหม่
        self.assertIn('FoodDetail', self.browser.title)
        table = self.browser.find_element_by_id('food_table')  
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1. ข้าวผัดหมู have sugar: 70 %', [row.text for row in rows])
        time.sleep(3)

        #โจ้พบว่าเขาใส่ระดับน้ำตาลของ "ข้าวผัดหมู" ผิด เขาจึงเข้าไปแก้ไขระดับน้ำตาลของ "ข้าวผัดหมู"
        inputbox = self.browser.find_element_by_id('old_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your old food')
        inputbox.send_keys('ข้าวผัดหมู')
        inputbox = self.browser.find_element_by_id('config_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your modify food')
        inputbox.send_keys('ข้าวผัดหมู')
        inputbox = self.browser.find_element_by_id('config_text_sugar')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your modify sugar')
        inputbox.send_keys('65')
        self.browser.find_element_by_id('submit_old_text_food').click()

        #เมื่อเขาเข้ามาที่ "Food Detail" โจ้จึงได้เห็นระดับน้ำตาลของอาหาร "ข้าวผัดหมู" ที่แก้ไขแล้ว
        table = self.browser.find_element_by_id('food_table')  
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1. ข้าวผัดหมู have sugar: 65 %', [row.text for row in rows])
        time.sleep(3)

        #โจ้คิดว่า "ข้าวผัดหมู" ก็ต้องบอกด้วยว่ามีผักหรือไม่มีผัก เขาจึงจะแก้ไขจาก "ข้าวผัดหมู" เป็น "ข้าวผัดหมูไม่ใส่ผัก"
        inputbox = self.browser.find_element_by_id('old_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your old food')
        inputbox.send_keys('ข้าวผัดหมู')
        inputbox = self.browser.find_element_by_id('config_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your modify food')
        inputbox.send_keys('ข้าวผัดหมูไม่ใส่ผัก')
        inputbox = self.browser.find_element_by_id('config_text_sugar')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your modify sugar')
        inputbox.send_keys('60')
        self.browser.find_element_by_id('submit_old_text_food').click()

        #เมื่อเขาเข้ามาที่ "Food Detail" โจ้จึงได้เห็นระดับน้ำตาลของอาหาร "ข้าวผัดหมูไม่ใส่ผัก" ที่แก้ไขแล้ว
        table = self.browser.find_element_by_id('food_table')  
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1. ข้าวผัดหมูไม่ใส่ผัก have sugar: 60 %', [row.text for row in rows])
        time.sleep(3)

        #โจ้ได้เพิ่ม "Coca-Cola have sugar: 80 %" เข้าไปอีกหนึ่งอย่าง 
        inputbox = self.browser.find_element_by_id('new_text_food')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your new food')
        inputbox.send_keys('Coca-Cola')
        inputbox = self.browser.find_element_by_id('new_text_sugar')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your sugar')
        inputbox.send_keys('80')
        self.browser.find_element_by_id('submit_new_text_food').click()
        
        #เมื่อเขาเข้ามาที่ "Food Detail" โจ้จึงได้เห็น "Coca-Cola have sugar: 80 %" ที่เขาเพิ่มเข้าไป
        table = self.browser.find_element_by_id('food_table')  
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('2. Coca-Cola have sugar: 80 %', [row.text for row in rows])
        
        time.sleep(5)
        self.fail('Finish the test!') 


if __name__ == '__main__': 
    unittest.main(warnings='ignore')


        
