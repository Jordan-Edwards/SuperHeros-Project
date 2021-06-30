from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Superhero


# Create your views here.

def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'SuperHeroesapp/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability,
                                  secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('SuperHerosapp:index'))
    else:
        return render(request, 'SuperHerosapp/create.html')


def change(request, superhero_id):
    specific_superhero = Superhero.objects.get(pk=superhero_id)
    context = {
        'specific_superhero': specific_superhero
    }
    if request.method == 'POST':
        change_name = request.POST.get('change_name')
        change_alter_ego = request.POST.get('change_alter_ego')
        change_primary_ability = request.POST.get('change_primary_ability')
        change_secondary_ability = request.POST.get('change_secondary_ability')
        change_catchphrase = request.POST.get('change_catchphrase')
        superhero_id = Superhero(name=change_name, alter_ego=change_alter_ego, primary_ability=change_primary_ability,
                                 secondary_ability=change_secondary_ability, catchphrase=change_catchphrase)
        superhero_id.save()
        return HttpResponseRedirect(reverse('SuperHerosapp:detail', context))
    else:
        return render(request, 'SuperHerosapp/change.html', context)


def delete(superhero_id):
    delete_superhero = Superhero.objects.get(pk=superhero_id)
    Superhero.delete(delete_superhero)
    return HttpResponseRedirect(reverse('SuperHerosapp:index'))


def detail(request, superhero_id):
    specific_superhero = Superhero.objects.get(pk=superhero_id)
    context = {
        'specific_superhero': specific_superhero
    }
    return render(request, 'SuperHerosapp/detail.html', context)
