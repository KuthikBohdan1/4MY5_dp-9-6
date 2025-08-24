from cofe_bar.models import Review, Register
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import ArticlesForm, Add_reviewsForm
def Reviews(request):

    review = Review.objects.all()

    context = {
        "all_review": review
    }

    return render(
        request,
        template_name="auth_system/index.html",
        context=context,
    )


def Register(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            print("1")
            form.save()
            return redirect('reviews')
        else:
            error = 'Неправильно введіні данні'
            print(error)


    form = ArticlesForm()

    
    context = {
        "all_form" : form,
        'error': error,
    }
    return render(
        request,
        template_name="auth_system/register_user.html",
        context=context,
    )

def Add_review(request):
    error = ''
    if request.method == 'POST':
        form = Add_reviewsForm(request.POST)
        if form.is_valid():
            print("успішно додано коментар")
            form.save()
            return redirect('reviews')
            
        else:
            error = 'Неправильно введіні данні'
            print(error)


    form = Add_reviewsForm()


    context = {
        "all_form": form
    }
    return render(
        request,
        template_name="auth_system/add_review.html",
        context=context,
    )





def Standart_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')  # або 'index', якщо є така сторінка
    else:
        form = UserCreationForm()
    
    return render(request, 'auth_system/standart_register.html', {'form': form})


