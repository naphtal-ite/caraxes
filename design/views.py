from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Author,Book
from .forms import LoginForm,UserRegisterForm,AuthorForm,BookForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_login(request):
    authors = Author.objects.all()
    if request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,
                      username=cd['username'],
                      password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request,user)
                messages.success(request,'Authenticated successfully')
                return redirect('author')
            else:
                messages.success(request,'Disabled account')
        else:
            messages.success(request,'Invalid login')
    else:
        form=LoginForm()
    return render(request,'home.html',{'form':form})

@login_required
def home(request):
    authors = Author.objects.all()
    context = {'authors':authors}
    return render(request,'author/author.html',context)


@login_required
def book(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request,'book/book.html',context)



@login_required
def about(request):
    return render(request,'about.html')

def user_logout(request):
    logout(request)
    messages.success(request,'you have been logged out')
    return redirect('/')


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = UserRegisterForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

@login_required
def add_record(request):
    if request.method == 'POST':
	    form = AuthorForm(request.POST)
	    if form.is_valid():
		    form.save()
		    messages.success(request, "You Have Successfully Registered! Welcome!")
		    return redirect('author')
    else:
       form = AuthorForm()
    return render(request, 'author/add.html', {'form':form})

	
@login_required
def update(request,pk):
    author=get_object_or_404(Author,pk=pk)
    if request.method =='POST':
        form=AuthorForm(request.POST,instance=author)
        if form.is_valid():
            form.save()
            messages.success(request,'record updated successfully')
            return redirect('author')
    else:
        form=AuthorForm(instance=author)
    return render(request,'author/update.html',{'form': form})

@login_required
def update_book(request,pk):
    book=get_object_or_404(Book,pk=pk)
    if request.method=='POST':
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            messages.success(request,'book updated successfully')
            return redirect('book')
    else:
        form=BookForm(instance=book)
    return render(request,'book/update_book.html',{'form':form})


@login_required
def add_book(request):
    if request.method=='POST':
       form = BookForm(request.POST or None)
       if form.is_valid():
          add = form.save()
          messages.success(request,'book created successfully')
    else:
        form = BookForm()
    return render(request, 'book/add_book.html', {'form':form})


def delete_book(request, pk):
	if request.user.is_authenticated:
		delete_it = Book.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Book Deleted Successfully...")
		return redirect('book')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def delete_author(request, pk):
	if request.user.is_authenticated:
		delete_it =Author.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "author Deleted Successfully...")
		return redirect('author')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')