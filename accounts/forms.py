from django.contrib.auth.forms import UserCreationForm

from accounts.models import Manager


class ManagerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Manager
        fields = UserCreationForm.Meta.fields + ("position",)
