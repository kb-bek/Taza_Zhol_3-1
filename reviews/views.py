from django.shortcuts import render
from .models import Review
from django.views import generic
from . forms import ReviewForm
from django.contrib import messages

def reviews(request):

    reviews_data = Review.objects.all()

    context = {
        'reviews': reviews_data
    }

    return render(request, 'reviews.html', context=context)




class ReviewSend(generic.FormView):
    template_name = "send_review.html"
    form_class = ReviewForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Спасибо за ваш отзыв')
        return super().form_valid(form)