from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from khubkhaoapp.models import Item,Veggie,Food

def IndexView(request):
    query_one = Food.objects.all()
    query_two = Item.objects.all()
    query_four = Veggie.objects.all()
    context = {
        'food_list': query_one,
        'category_list': query_two,
        'vegie_list': query_four,
    }
    return render(request, 'khubkhaoapp/index.html', context)



