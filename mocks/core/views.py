from django.shortcuts import render

from mocks.core.models import Congressperson


def home(request):
    context =  {'congresspeople': Congressperson.objects.all()}
    return render(request, 'core/index.html', context=context)
