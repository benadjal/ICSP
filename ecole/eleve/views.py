from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)
def inscription(request):
	return render(request,'eleve/inscription.html', locals())

def addition(request, x, y):
	somme = x + y
	return render(request,'eleve/addition.html', locals())	
