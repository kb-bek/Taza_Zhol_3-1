from django.shortcuts import render
from .models import New

def news(request):
    news_data = New.objects.all()

    context = {
        'news': news_data
    }
    return render(request, 'news.html', context=context)