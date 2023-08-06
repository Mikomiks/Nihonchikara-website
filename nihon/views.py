from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.db import connection
from wsgiref.util import FileWrapper
import mimetypes
import os 

from django.contrib.auth.decorators import login_required

from .decorators import allowedusers, unauthenticated_user

from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm




def landing(request):
    return render(request,"nihon/index.html")

def home(request):
    return render(request,"nihon/sign-out-page.html")

def logoutUser(request):
    logout(request)
    del request
    return redirect('/')

@unauthenticated_user
def plogin(request):
    
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            

    context = {}
    return render(request, "nihon/sign-in.html",context)

@unauthenticated_user
def preg(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account is succeffuly created!, Iku zo')
            return redirect('login')
        
        
    context= {'form':form}

    return render(request, "nihon/sign-up.html", context)

@login_required(login_url='login')
def course(request):
    return render(request, "nihon/courses.html")

@login_required(login_url='login')
def learn(request):
    return render(request, "nihon/downloadables.html")

@login_required(login_url='login')
def learn2(request):
    return render(request, "nihon/downloadables2.html")

@login_required(login_url='login')
@allowedusers(allowed_roles=['student','admin'])
def download_file(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Katakana Practice.pdf'
    filepath = base_dir + '/nihon/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type=mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "attachment;filename=%s" %filename
    return response

@login_required(login_url='login')
@allowedusers(allowed_roles=['student','admin'])
def download_file1(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Combination Hiragana.pdf'
    filepath = base_dir + '/nihon/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type=mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "attachment;filename=%s" %filename
    return response

@login_required(login_url='login')
@allowedusers(allowed_roles=['student','admin'])
def download_file2(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'hiragana CHART.jpg'
    filepath = base_dir + '/nihon/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type=mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "attachment;filename=%s" %filename
    return response

@login_required(login_url='login')
@allowedusers(allowed_roles=['student','admin'])
def download_file3(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Hiragana Practice #1.pdf'
    filepath = base_dir + '/nihon/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type=mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "attachment;filename=%s" %filename
    return response

@login_required(login_url='login')
@allowedusers(allowed_roles=['student','admin'])
def download_file4(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Hiragana Practice #2.pdf'
    filepath = base_dir + '/nihon/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type=mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "attachment;filename=%s" %filename
    return response

@login_required(login_url='login')
@allowedusers(allowed_roles=['student','admin'])
def download_file5(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'hiragana-mnemonic-chart-by-tofugu.jpg'
    filepath = base_dir + '/nihon/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type=mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "attachment;filename=%s" %filename
    return response

@login_required(login_url='login')
@allowedusers(allowed_roles=['student','admin'])
def download_file6(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'tofugu-katakana-chart.jpg'
    filepath = base_dir + '/nihon/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type=mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "attachment;filename=%s" %filename
    return response

@login_required(login_url='login')
@allowedusers(allowed_roles=['student','admin'])
def download_file7(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'tofugu-katakana-mnemonic-chart.jpg'
    filepath = base_dir + '/nihon/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type=mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "attachment;filename=%s" %filename
    return response

@login_required(login_url='login')
@allowedusers(allowed_roles=['student','admin'])
def download_file8(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Assets.gif'
    filepath = base_dir + '/nihon/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type=mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "attachment;filename=%s" %filename
    return response