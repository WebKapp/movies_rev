from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return render(request, 'reviews/index.html')


def add_review_view(request):
    return render(request, 'reviews/add_review.html')

