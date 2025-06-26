from cofe_bar.models import Review, Register_user_data
from django.shortcuts import render, redirect

from .forms import ArticlesForm
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
            form.save()
            return redirect('reviews')
        else:
            error = 'Неправильно введіні данні'
            print(error)


    form = ArticlesForm()

    
    context = {
        "all_form" : form,
        'error': error
    }
    return render(
        request,
        template_name="auth_system/register_user.html",
        context=context,
    )