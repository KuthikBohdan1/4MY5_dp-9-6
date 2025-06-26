from .models import Register_user_data
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesForm(ModelForm):

    class Meta:
        model = Register_user_data
        fields = ['name', 'password', 'return_password', 'user_birth_date']
        # fields = []
        widgets = {
            'name' : TextInput(attrs={
                'class': 'form-control_username',
                'placeholder': 'псевдонім ',
            }),
            'password' : TextInput(attrs={
                'class': 'form-control_password',
                'placeholder': 'пароль',
            }),
            'return_password' : TextInput(attrs={
                'class': 'form-control_return_password',
                'placeholder': 'пароль 2',
            }),
            'user_birth_date' : DateTimeInput(attrs={
                'class': 'form-control_date',
                'type': 'datetime-local'
            })


        }