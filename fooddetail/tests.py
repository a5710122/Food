from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from fooddetail.models import Food


class HomePageTest(TestCase):

    def test_quiz_page_template(self):
        response = self.client.get('/fooddetail/')
        self.assertTemplateUsed(response, 'fooddetail/index.html')

    def test_quiz_page_returns_correct_html(self):
        response = self.client.get('/fooddetail/')  

        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>FoodDetail</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'fooddetail/index.html')

    def test_displays_all_list_question(self):
        response = self.client.get('/fooddetail/add_food')
        Food.objects.create(food_text='ข้าวมันไก่', number_sugar = 65)
        Food.objects.create(food_text='ไก่ทอด', number_sugar = 78)
        response = self.client.get('/fooddetail/')
        self.assertIn('ข้าวมันไก่', response.content.decode())
        self.assertIn('ไก่ทอด', response.content.decode())


       



    
