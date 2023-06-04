from django.shortcuts import get_object_or_404, render, redirect
from account import models as accountModels
from . import models
# Create your views here.


def home(request):

    context = {
        'book': models.Book.objects.all(),
    }

    return render(request, 'home.html', context=context)


def single(request, id):
    context = {
        'book': models.Book.objects.get(id),
        'current_user': accountModels.User.objects.get(is_authenticated=True),

    }
    return render(request, 'single.html', context)


def borrow(request, id):
    if request.method == "POST":
        this_book = models.Book.objects.get(pk=id)
        if this_book.quantity != 0:
            # book_inst = Models.BookInstance(book=this_book.id, borrower=current_user.id) make a instanceBook with id of book and user
            # this_book.quantity -= 1
            # book_inst.status = 'o'
            # app.db.session.add(book_inst)
            # app.db.session.commit()
            # flash('You Borrowed This Book', 'success')
            return redirect('single.html', {id: id})
        else:
            # flash("There is not any version if this book at this moment", 'warning')
            return redirect('single.html', {id: id})


def search(request):
    pass


def categories(request, name):
    pass
