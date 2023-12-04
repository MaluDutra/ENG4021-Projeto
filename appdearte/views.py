from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template.loader import get_template
from .models import Events, Category, Price, Time
from .forms import AvaliationForm, EventsForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required #troço de avaliação
from appdearte import scrape

# Create your views here.
@csrf_protect
def homepage(request):
  events = Events.objects.all()
  scrape.scrape_events()
  return render(request, "homepage.html", context = {
                 "events" : events
               })

#filtros
#FAZER TROÇO DE CARREGAR EVENTOS SOMENTE VALIDADOS
def searchpage(request):
  qs = Events.objects.all()

  if request.method == "POST":
    name_contains_query = request.POST.get("event_name")
    price_contains_query = request.POST.get("preço")
    time_contains_query = request.POST.get("horário")
    category_contains_query = request.POST.get("rolê")

    if name_contains_query:
      qs = qs.filter(name__icontains=name_contains_query)
    if price_contains_query and price_contains_query != "-":
      qs = qs.filter(price__icontains=price_contains_query)
    if time_contains_query and time_contains_query != "-":
      qs = qs.filter(time__name=time_contains_query)
    if category_contains_query and category_contains_query != "-":
      qs = qs.filter(categories__name=category_contains_query)
    qs = qs.filter(validated=True)
    return render(request, "searchpage.html",context = { "search":  
      name_contains_query, "queryset" : qs})

def know_more(request):
  return render(request,"moreabout.html")

def avaliation_form(request, pk):
  event = Events.objects.get(id=pk)
  event_name=event.name
  user = request.user
  print(user)
  form = AvaliationForm(instance=event)
  if request.method == "POST":
      form = AvaliationForm(request.POST, instance=event)
      if form.is_valid():
        form.save()
        return redirect("home")
  if request.user.is_authenticated:
    return render(request, "avaliation.html", {"form": form, "event_name": event_name})
  else:
    return login_user(request, "Você precisa estar logado para avaliar um evento")

#adicionar evento
def add_event(request):
  form = EventsForm()
  if request.method == "POST":
    form = EventsForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("home") 
  if request.user.is_authenticated:
    return render(request, "addevent.html", context={"form":form})
  else:
    return login_user(request, "Você precisa estar logado para adicionar um evento")

#parte do credenciamento
def create_user(request):
  if request.method == "POST":
    if User.objects.filter(username = request.POST['username']).first():
      return render(request, "register.html", context={"error_msg": "Username já existe! =c"})
    if User.objects.filter(email = request.POST['email']).exists():
      return render(request, "register.html", context={"error_msg": "Email já cadastrado! =c"})
    if request.POST["username"] =='' or request.POST["email"] =='' or request.POST["password"] =='':
      return render(request, "register.html", context={"error_msg": "Por favor, preencha todos os campos adequadamente! >:C"})
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"],
      request.POST["password"]      
    )    
    user.save()
    login(request, user)
    return redirect("home")
  return render(request,"register.html")

def login_user(request, error_msg):
  if request.method =="POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"] 
    )
    if user != None:
      login(request, user)
    elif User.objects.filter(username = request.POST['username']).exists():
      return render(request,"login.html",context={"error_msg":"Usuário não conseguiu ser logado! =c"})
    else:
      return render(request,"login.html",context={"error_msg":"Usuário não encontrado! =c"})
    if request.user.is_authenticated:
      return redirect("home")
  if error_msg=="Você precisa estar logado para adicionar um evento":
    return render(request,"login.html",context={"error_msg": "Você precisa estar logado para adicionar um evento"})
  elif error_msg=="Você precisa estar logado para avaliar um evento":
    return render(request,"login.html",context={"error_msg": "Você precisa estar logado para avaliar um evento"})
  return render(request,"login.html")

def logout_user(request):
  logout(request)
  return redirect("home")