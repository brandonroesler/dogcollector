from django.shortcuts import render

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Tony', 'Toy Fox Terrier', 'Cutest dog in the world', 7),
    Dog('Miles', 'Puggle', 'A bit aggressive with the ball', 7),
    Dog('Mia', 'Chihuahua', "Don't really know her that well yet", 2)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })