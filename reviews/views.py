from django.shortcuts import render, get_object_or_404, redirect
from reviews.models import Machine, Personnel
from reviews.forms import AddMachineForm, AddPersonnelForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def register(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.sucess(request, 'Le compte a été créé')
            return redirect('login')
    context = {'form' : form}
    return render(request,'users/register.html', context)

def login(request):
    context = {}
    if request.method=='POST':
        username = request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else : 
            messages.info(request, 'utilisateur et mot de passe incorrect')
    return render(request, 'users/login.html', context)


def index(request) :
    context = {}
    return render(request, 'index.html', context)

def machine_list_view(request) :
    machines=Machine.objects.all()
    context={'machine': machines}
    return render(request, 'app/machine_list.html', context)

def personnel_list_view(request) :
    persos=Personnel.objects.all()
    context={'employe': persos}
    return render(request, 'app/personnel_list.html', context)

def machine_detail_view(request,pk) :
    machine = get_object_or_404(Machine, id=pk)
    context = {'machine-detail': machine}
    return render(request,'app/machine_detail.html',context)

def personnel_detail_view(request,pk) :
    perso = get_object_or_404(Personnel, num_secu=pk)
    context = {'employe-detail': perso}
    return render(request,'app/personnel_detail.html',context)

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid() :
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')
    else :
        form = AddMachineForm()
        context = {'form': form}
        return render (request ,'app/machine_add.html',context)

def personnel_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST or None)
        if form.is_valid() :
            new_personnel = Personnel(nom=form.cleaned_data['nom'])
            new_personnel.save()
            return redirect('personnels')
    else :
        form = AddMachineForm()
        context = {'form': form}
        return render (request ,'app/personnel_add.html',context)

def deleteMachine(request, my_id):
    obj = get_object_or_404(Machine,id=my_id)
    obj.delete()
    redirect('machine')

def deletePersonnel(request, my_id):
    obj = get_object_or_404(Personnel,num_secu=my_id)
    obj.delete()
    redirect('employe')
    

