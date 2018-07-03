from django.shortcuts import render

from .models import Food

def index(request):
   food_list = Food.objects.order_by('id').values('food_text', 'number_sugar')
   count_food = Food.objects.count
   
   #print(sugar_list)


   context = {
           'food_list_to_html': food_list,
           'count_food_to_html' : count_food
   }
   return render(request, 'fooddetail/index.html', context)

def add_food(request):
   
   new_food = ''
   new_sugar = ''
   count_food = Food.objects.count
      
   if request.method == 'POST':
     new_food = request.POST['new_text_food']
     new_sugar = request.POST['new_text_sugar']

     if(new_food == ''):
        return render(request, 'fooddetail/error_message.html', { 'error_message_1': "You do not have food.", 'error_message_2': "Please check you Food input." })
     elif(new_sugar == ''):
        return render(request, 'fooddetail/error_message.html', { 'error_message_1': "You do not have food.", 'error_message_2': "Please check you Sugar input." })

     else:
        f = Food(food_text = new_food, number_sugar = new_sugar)
        f.save()
     

   food_list = Food.objects.order_by('id').values('food_text', 'number_sugar')
   
   context = {
           'food_list_to_html': food_list,
           'count_food_to_html' : count_food
   } 
   
   return render(request, 'fooddetail/index.html', context)


def delete_food(request):

    delete_food = ''
    count_food = Food.objects.count
    
    if request.method == 'POST':
       delete_food = request.POST['delete_text_food']
    
       check = Food.objects.filter(food_text=delete_food)
       #print(check)
   
       if(delete_food == ''):
          return render(request, 'fooddetail/error_message.html', { 'error_message_1': "No food you want to remove.", 'error_message_2': "You did not enter the input." })

       else:
          f = Food.objects.filter(food_text=delete_food)
          f.delete()

     
    food_list = Food.objects.order_by('id').values('food_text', 'number_sugar')
   
    context = {
           'food_list_to_html': food_list,
           'count_food_to_html' : count_food          
    } 
   
    return render(request, 'fooddetail/index.html', context)

def config_food(request):

    old_food = ''
    config_food = ''
    config_suger = ''
    count_food = Food.objects.count

    if request.method == 'POST':
     old_food = request.POST['old_text_food']
     config_food = request.POST['config_text_food']
     config_suger = request.POST['config_text_sugar']

     check_old_food = Food.objects.get(food_text=old_food)
     
     
     if(old_food == ''):
        return render(request, 'fooddetail/error_message.html', { 'error_message_1': "You do not have food.", 'error_message_2': "Please check you input." })
     

     elif(config_food == ''):
        return render(request, 'fooddetail/error_message.html', { 'error_message_1': "You do not have food.", 'error_message_2': "Please check you input." })

     elif(config_suger == ''):
        return render(request, 'fooddetail/error_message.html', { 'error_message_1': "You do not have food.", 'error_message_2': "Please check you input." })

     
     else:
        f = Food.objects.get(food_text=old_food)
        f.food_text = config_food
        f.number_sugar = config_suger
        f.save()

    food_list = Food.objects.order_by('id').values('food_text', 'number_sugar')
   
    context = {
           'food_list_to_html': food_list,
           'count_food_to_html' : count_food          
    } 
   
    return render(request, 'fooddetail/index.html', context)

