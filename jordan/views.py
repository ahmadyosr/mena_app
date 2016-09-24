
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AlbumsForm
from .models import Albums
from django.contrib.auth.decorators import login_required 

# Create your views here.

@login_required
def index(request):
	
	if request.method == 'POST':
		form=AlbumsForm(request.POST)
		if form.is_valid():
			item=form.save(commit=False)
			item.save()
			return redirect('index')
	else:
			form=AlbumsForm()
			
	return render(request,'jordan/index.html',{'form':form})
	
	
