from django import forms
from django.contrib.auth.models import User


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'groups', 'is_superuser', 'is_staff', 'is_active')
        widgets = {'groups': forms.SelectMultiple,}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].help_text='Обязательное поле. Введите ваше имя или название компании'
        self.fields['first_name'].required=True
        self.fields['username'].label='Логин'
        self.fields['groups'].help_text='Группа, к которой принадлежит данный пользователь. Пользователь получит все ' \
                                        'права, указанные в группе.'
        self.fields['groups'].label='Роль (группа)'

    def clean_groups(self):
        groups = self.cleaned_data['groups']
        if len(groups) > 1:
            raise forms.ValidationError(f"Выберите не более 1 позиции")
        return groups


class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email', 'groups', 'is_superuser', 'is_staff', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].help_text='Обязательное поле. Введите ваше имя или название компании'
        self.fields['first_name'].required=True
        self.fields['username'].label='Логин'
        self.fields['groups'].help_text='Группа, к которой принадлежит данный пользователь. Пожалуйста выберите только ' \
                                        'одну из групп. Пользователь получит все права, указанные в группе. Тонкую ' \
                                        'настройку прав самой группы вы можете сделать в административной части сайта ' \
                                        '(/admin).'
        self.fields['groups'].label='Роль (группа)'
        self.fields['groups'].required=True
