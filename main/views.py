from django.shortcuts import render, reverse
from .forms import TestForm, TestForm2
from .models import Test
from django.views.generic import CreateView, UpdateView, DeleteView


def home(request):
    is_valid = False
    form = TestForm()

    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            birth = form.cleaned_data.get('birth')
            Test.objects.create(name=name, age=age, birth=birth)
            is_valid = True
    return render(request, 'home.html', {'form': form, 'is_valid': is_valid})


def home2(request):
    is_valid = False
    form = TestForm2()

    if request.method == 'POST':
        form = TestForm2(request.POST)
        if form.is_valid():
            form.save()
            is_valid = True
    return render(request, 'home.html', {'form': form, 'is_valid': is_valid})


class TestCreateView(CreateView):
    form_class = TestForm2()
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('home')


# def home(request):
#     if request.method == 'POST':
#         form = TestForm(request.POST)
#         if form.is_valid():
#             return render(request, 'home.html', {'is_valid': True})
#         else:
#             return render(request, 'home.html', {'form': form})
#
#     return render(request, 'home.html', {'form': TestForm})
