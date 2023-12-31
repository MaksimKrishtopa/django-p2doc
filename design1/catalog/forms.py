# forms.py


from django import forms
from .models import DesignRequest
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from .models import UserProfile

from django import forms
from .models import DesignRequest, DesignCategory


@deconstructible
class FIOValidator(validators.RegexValidator):
    regex = r"^[а-яА-Я\s-]+$"
    message = "Введите корректное ФИО. Значение может содержать только кириллические буквы, пробелы и тире."


@deconstructible
class LoginValidator(validators.RegexValidator):
    regex = r"^[a-zA-Z-]+$"
    message = "Введите корректный логин. Значение может содержать только латинские буквы и тире."


class UserProfileForm(forms.ModelForm):
    fio = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'ФИО'}),
        label='ФИО',
        validators=[FIOValidator()],
    )

    class Meta:
        model = UserProfile
        fields = ['fio']
        labels = {'fio': 'ФИО'}


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    agree_to_processing = forms.BooleanField(required=True,
                                             widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    fio = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'ФИО'}),
        label='ФИО',
        validators=[FIOValidator()],
    )

    class Meta:
        model = User
        fields = ['fio', 'username', 'email', 'password1', 'password2', 'agree_to_processing']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
            'agree_to_processing': 'Согласие на обработку персональных данных',
            'fio': 'ФИО',
        }
        field_order = ['fio', 'username', 'email', 'password1', 'password2', 'agree_to_processing']

    def clean_username(self):
        username = self.cleaned_data['username']
        validator = LoginValidator()
        try:
            validator(username)
        except ValidationError:
            raise forms.ValidationError(validator.message)

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Этот логин уже занят. Пожалуйста, выберите другой.')

        return username


class DesignRequestForm(forms.ModelForm):
    class Meta:
        model = DesignRequest
        fields = ['title', 'category', 'description', 'photo']


class CreateDesignRequestForm(forms.ModelForm):
    class Meta:
        model = DesignRequest
        fields = ['title', 'category', 'description', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }


class DesignCategoryForm(forms.ModelForm):
    class Meta:
        model = DesignCategory
        fields = ['name']
        labels = {'name': ('Название категории')}



# forms.py

from django import forms
from .models import DesignRequest
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from .models import UserProfile

from django import forms
from .models import DesignRequest, DesignCategory


@deconstructible
class FIOValidator(validators.RegexValidator):
    regex = r"^[а-яА-Я\s-]+$"
    message = "Введите корректное ФИО. Значение может содержать только кириллические буквы, пробелы и тире."


@deconstructible
class LoginValidator(validators.RegexValidator):
    regex = r"^[a-zA-Z-]+$"
    message = "Введите корректный логин. Значение может содержать только латинские буквы и тире."


class UserProfileForm(forms.ModelForm):
    fio = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'ФИО'}),
        label='ФИО',
        validators=[FIOValidator()],
    )

    class Meta:
        model = UserProfile
        fields = ['fio']
        labels = {'fio': 'ФИО'}


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    agree_to_processing = forms.BooleanField(required=True,
                                             widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    fio = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'ФИО'}),
        label='ФИО',
        validators=[FIOValidator()],
    )

    class Meta:
        model = User
        fields = ['fio', 'username', 'email', 'password1', 'password2', 'agree_to_processing']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
            'agree_to_processing': 'Согласие на обработку персональных данных',
            'fio': 'ФИО',
        }
        field_order = ['fio', 'username', 'email', 'password1', 'password2', 'agree_to_processing']

    def clean_username(self):
        username = self.cleaned_data['username']
        validator = LoginValidator()
        try:
            validator(username)
        except ValidationError:
            raise forms.ValidationError(validator.message)

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Этот логин уже занят. Пожалуйста, выберите другой.')

        return username


class DesignRequestForm(forms.ModelForm):
    class Meta:
        model = DesignRequest
        fields = ['title', 'category', 'description', 'photo']


class CreateDesignRequestForm(forms.ModelForm):
    class Meta:
        model = DesignRequest
        fields = ['title', 'category', 'description', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }


class DesignCategoryForm(forms.ModelForm):
    class Meta:
        model = DesignCategory
        fields = ['name']
        labels = {'name': ('Название категории')}


class ChangeStatusForm(forms.ModelForm):
    class Meta:
        model = DesignRequest
        fields = ['status']

    status = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')

        if status == 'Принято в работу' and not self.instance.comment:
            raise forms.ValidationError({'status': 'Добавьте комментарий для статуса "Принято в работу".'})
        elif status == 'Выполнено' and not self.instance.photo:
            raise forms.ValidationError({'status': 'Добавьте изображение дизайна для статуса "Выполнено".'})
        return cleaned_data


class CompleteDesignForm(forms.ModelForm):
    design_image = forms.ImageField(label='Изображение дизайна', required=True)
    comment = forms.CharField(widget=forms.Textarea, label='Комментарий', required=True)

    class Meta:
        model = DesignRequest
        fields = []
