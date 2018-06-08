from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm

def index(request):
    all_entries=Entry.objects.all()
    return render(request,'app/index.html',{'all_entries':all_entries})

@login_required
def calendar(request):
    all_entries=Entry.objects.filter(author=request.user).order_by('date')
    return render(request,'app/calendar.html',{'all_entries':all_entries})

@login_required
def details(request,entry_id):
    current_entry=get_object_or_404(Entry,pk=entry_id)
    return render(request,'app/details.html',{'current_entry':current_entry})

@login_required
def favorite_entry(request,entry_id):
    current_entry=get_object_or_404(Entry,pk=entry_id)

    if current_entry.is_favorite:
        current_entry.is_favorite=False
    else:
        current_entry.is_favorite=True

    current_entry.save()

    return render(request,'app/details.html',{'current_entry':current_entry})

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            date=form.cleaned_data['date']
            description=form.cleaned_data['description']
            Entry.objects.create(name=name,author=request.user,date=date,description=description).save()
            return HttpResponseRedirect('/calendar/')
    else:
        form = EntryForm()

    return render(request, 'app/add_entry.html', {'form': form})

@login_required
def remove(request,entry_id):
    entry=get_object_or_404(Entry,pk=entry_id)
    entry.delete()
    return HttpResponseRedirect('/calendar/')

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']

            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/calendar/')

    else:
        form=UserCreationForm()

    return render(request,'registration/register.html',{'form':form})
