from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Book, Review
from django.urls import reverse
# Create your views here.
def home(request):
    data = Book.objects.all()
    return render(request,'book/index.html',{"books":data})

def review(request,id):
    book=Book.objects.get(id=id)
    review=Review.objects.filter(book=book)
    return render(request,'book/review.html',{"book":book, "reviews":review})

def hemant(request,id):
    review_name=request.POST.get('reviewsname')
    review_ratings=request.POST.get('reviewsratings')
    review_body=request.POST.get('reviewbody')
    book=Book.objects.get(id=id)
    review_obj=Review(book=book,name=review_name, ratings= review_ratings,review=review_body)
    review_obj.save()
    return HttpResponseRedirect(reverse('book:review', args=(id)) )