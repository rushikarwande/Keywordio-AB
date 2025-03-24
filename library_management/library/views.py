from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .models import Admin, Book
from django.http import HttpResponse

# Admin Signup
def admin_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))

        # Check if admin with the same email already exists
        if not Admin.objects.filter(email=email).exists():
            Admin.objects.create(name=name, email=email, password=password)
            return redirect('admin_login')
        else:
            return HttpResponse("Admin with this email already exists.")
    return render(request, 'admin_signup.html')

# Admin Login
def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        admin = Admin.objects.filter(email=email).first()

        # Check if admin exists and password is correct
        if admin and check_password(password, admin.password):
            request.session['admin_id'] = admin.id  # Store admin ID in session
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid email or password.")
    return render(request, 'admin_login.html')

# Add Book
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        published_date = request.POST.get('published_date')
        quantity = request.POST.get('quantity')

        # Create a new book entry
        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            published_date=published_date,
            quantity=quantity
        )
        return redirect('dashboard')
    return render(request, 'add_book.html')

# View All Books
def view_books(request):
    books = Book.objects.all()
    return render(request, 'view_books.html', {'books': books})

# Update Book
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.isbn = request.POST.get('isbn')
        book.published_date = request.POST.get('published_date')
        book.quantity = request.POST.get('quantity')
        book.save()
        return redirect('view_books')
    return render(request, 'update_book.html', {'book': book})

# Delete Book
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('view_books')