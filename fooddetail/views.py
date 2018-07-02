from django.shortcuts import render

from .models import Food

def index(request):
   food_list = Food.objects.order_by('id').values('food_text', 'number_sugar')
   
   
   #print(sugar_list)


   context = {
           'food_list_to_html': food_list
           
   }
   return render(request, 'fooddetail/index.html', context)

def add_food(request):
   
   new_food = ''
   new_sugar = ''
      
   if request.method == 'POST':
     new_food = request.POST['new_text_food']
     new_sugar = request.POST['new_text_sugar']
     f = Food(food_text = new_food, number_sugar = new_sugar)
     f.save()
     

   food_list = Food.objects.order_by('id').values('food_text', 'number_sugar')
   
   context = {
           'food_list_to_html': food_list
           
   } 
   
   return render(request, 'fooddetail/index.html', context)


def delete_food(request):

    delete_food = ''
    
    if request.method == 'POST':
     delete_food = request.POST['new_text_food']
     
     f = Food.objects.filter(food_text=delete_food)
     f.delete()
     

    food_list = Food.objects.order_by('id').values('food_text', 'number_sugar')
   
    context = {
           'food_list_to_html': food_list          
    } 
   
    return render(request, 'fooddetail/index.html', context)


