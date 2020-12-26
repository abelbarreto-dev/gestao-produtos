from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def home(request):
    """
        chama a página principal
        abelbcarvalho
    """
    return render(request, 'home.html')

def logout_made(request):
    """
        sai da conta de usupário adm
        abelbcarvalho
    """
    logout(request)
    return redirect('home')
