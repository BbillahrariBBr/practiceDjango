from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel

# Create your views here.
def home(request):
    return render(request, 'store_book.html')

def store_book(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('showbook')
            # book = BookStoreForm()
    else:
        book = BookStoreForm()
    return render(request,'store_book.html',{'form':book})

def show_book(request):
    book = BookStoreModel.objects.all()
    for item in book:
        
        print(item.first_pub)
        print(item.last_pub)
    return render(request,'show_book.html',{'data':book})
    
    
