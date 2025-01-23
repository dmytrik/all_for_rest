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
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name"
        )


class ManagerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )
