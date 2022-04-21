from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import NewBookForm,NewReviewForm
from .models import Books,Review,Profile

# Create your views here.
# @login_required(login_url='/accounts/register/')
def index(request):
    return render (request,'all-books/home.html')

def library(request):
    current_user = request.user
    books = Books.objects.all()
    return render(request,'all-books/books.html',{"books":books,"current_user":current_user})


def new_book(request):
    current_user = request.user
    if request.method == "POST":
        form = NewBookForm(request.POST,request.FILES)
        form.instance.admin = request.user
        print(form)
        if form.is_valid():

            form.save()
            return redirect('library')

    else:
        form = NewBookForm()
        
    return render(request,'all-books/newbook.html',{"form":form})


def book_details(request,id):
    novels = Books.objects.get(id=id)
    reviews = Review.objects.filter(book=novels)

    return render(request,'all-books/details.html',{"novels":novels,"reviews":reviews})

def new_review(request,id):
    current_user = request.user
    if request.method == 'POST':
        review_form = NewReviewForm(request.POST)
        if review_form.is_valid():
            review_form.instance.user = request.user
            review_form.author = Books.objects.filter(id=id)
            review_form.save()

            next = request.GET.get('next',reverse('library'))
            return  HttpResponseRedirect(f'/my_book/{id}')
        
    else:
        review_form = NewReviewForm()

    return render(request,'all-books/review.html',{"review_form":review_form})