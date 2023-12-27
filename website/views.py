from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddProjectForm
from .models import Records

def home(request):
    record = Records.objects.all()

    # Kijk of er aangemeld is.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Autorisatie
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Je bent met succes aangemeld!")
            return redirect('home')
        else:
            messages.success(request, "Er is een fout onstaan bij het aanmelden, probeer opnieuw...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'record': record})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Je bent afgemeld...")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Je bent succesvol gereigistreed! Welkome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def project_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		project_record = Records.objects.get(id=pk)
		return render(request, 'record.html', {'project_record':project_record})
	else:
		messages.success(request, "Je moet aangemeld zijn om deze pagina te zien...")
		return redirect('home')

def delete_project(request, pk):
    if request.user.is_authenticated:
        delete_it = Records.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Je hebt het geselecteerde project succesvol gewist...")
        return redirect('home')
    else:
        messages.success(request, "Je moet ingelogd zijn om gegevens te kunnen bewerken...")
        return redirect('home')

def add_project(request):
    form = AddProjectForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_project = form.save()
                messages.success(request, "Project Toegevoegd...")
                return redirect('home')

        return render(request, 'add_project.html', {'form':form})
    else:
        messages.success(request, "Je moet ingelogd zijn om gegevens in te voeren...")
        return redirect('home')

def update_project(request, pk):
    if request.user.is_authenticated:
        current_record = Records.objects.get(id=pk)
        form = AddProjectForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Het project is gewijzigd...")
            return redirect('home')
        return render(request, 'update_project.html', {'form':form})
    else:
        messages.success(request, "Je moet ingelogd zijn om gegevens in te voeren...")
        return redirect('home')
