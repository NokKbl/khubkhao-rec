from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from khubkhaoapp.models import Item,Veggie,Food

def IndexView(request):
    query_one = Food.objects.all()
    query_two = Item.objects.all()
    query_three = Food.objects.get(id=2)
    query_four = Veggie.objects.all()
    query_five = Food.objects.all()
    context = {
        'query_one': query_one,
        'query_two': query_two,
        'title': query_three,
        'query_four': query_four,
        'query_five': query_five,
    }
    return render(request, 'khubkhaoapp/index.html', context)



