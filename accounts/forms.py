from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import Manager


class ManagerCreationForm(UserCreationForm):

    position = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Manager.TYPE_POSITION
    )

    class Meta(UserCreationForm.Meta):
        model = Manager
        fields = UserCreationForm.Meta.fields + ("position",)
