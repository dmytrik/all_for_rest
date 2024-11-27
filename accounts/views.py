from django.shortcuts import render
from django.views import generic

from accounts.models import Manager


class ManagerListView(generic.ListView):
    model = Manager
