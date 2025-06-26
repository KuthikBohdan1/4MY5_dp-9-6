from .models import Register, Review,Standart
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateInput
from django.contrib.auth.forms import  UserCreationForm
class ArticlesForm(ModelForm):

    class Meta:
        model = Register
        fields = ['name', 'password', 'return_password', 'user_birth_date']
        # fields = []
        widgets = {
            'name' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'псевдонім ',
            }),
            'password' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'пароль',
            }),
            'return_password' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'пароль 2',
            }),
            'user_birth_date' : DateInput(attrs={
                'class': 'form-control',
                # 'type': 'datetime-local'
            })


        }

class Add_reviewsForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title','content','author','pub_date']
        widgets = {
            'title' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'опис ',
            }),
            'content' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'контент',
            }),
            'author' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'опис ',
            }),
            'pub_date' : DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),


        
        }

# class StandartForm(ModelForm):
#     class Meta:
#         model = Register
#         fields = Standart
#         fields = UserCreationForm.Meta.fields