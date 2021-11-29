from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)