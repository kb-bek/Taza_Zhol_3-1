from django.shortcuts import render
from news.models import New
from reviews.models import Review

def index(request):
    news_data = New.objects.all()
    reviews_data = Review.objects.all()

    context = {
        'reviews': reviews_data,
        'news': news_data
    }


    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'news.html')


def price(request):
    return render(request, 'reviews.html')

def blog_detail(request):
    return render(request, 'single.html')

def contact(request):
    return render(request, 'contact.html')