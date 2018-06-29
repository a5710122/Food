from django.shortcuts import render

from .models import Food, Detail

def index(request):
   food_list = Food.objects.order_by('id')
   sugar_list = Food.objects.order_by('id')

   new_food = ''
   
   if request.method == 'POST':
     new_food = request.POST['new_text_food']
     f = Food(food_text = new_food)
   
   context = {
           'food_list_to_html': food_list,
           'sugar_list_to_html' : sugar_list
   }
   return render(request, 'fooddetail/index.html', context)




