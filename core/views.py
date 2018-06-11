from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Teams, Users

# Create your views here.
def signup(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

        else:
            form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def index(request):

    num_Teams = Teams.objects.all().count()
    num_Users = Users.objects.all().count()

    return render(request, 'core/home_page.html', context={'num_Teams': num_Teams, 'num_Users':num_Users})

def choose(request):
    return render(request, 'core/choose.html')

def thx(request):
    return render(request, 'core/thank4reg.html')

def our_log(request):
    return render(request, 'core/index.html')

def druzyna(request):
    return render(request, 'core/druzyna.html')

def pan_trenera(request):

    all_Teams = Teams.objects.all()

    return render(request, 'core/panel_trenera.html', context={'all_Teams': all_Teams})

def pan_zawodnika(request, id_team):
    team = get_object_or_404(Teams, pk=id_team)
    return render(request, 'core/strona_glowna.html', {'team':team})

def user_page(request, user_id):
    return HttpResponse("Strona usera o id %s." % user_id)

def player_page(request, user_player_id):
    return HttpResponse('Strona dla zawodnika o id %s.' % user_player_id)

def team_page(requset, team_id):
    return HttpResponse('Strona druzyny o id %s.' % team_id)
