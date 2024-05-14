from django.shortcuts import render, redirect
from .forms import RegistrationForm

def olympaid(request):
    return render(request, 'olympaid_app/olympaid.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = RegistrationForm()

    return render(request, 'olympaid_app/register.html', {'form': form})
   

