from django.shortcuts import render, redirect
from django,contrib,auth import authenticate, login

def login_view(request)
    if request.method == 'POST'
        username= request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        
        if user is not none:
            login(request, user)
            return redirect('home')
        else:
            erorr_massage='name karbari eshtebah ast.'
    else:
        error_massage=''
    return render(request, 'login.html')
