from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Menu


def index(request):
    # return HttpResponse("Hello World. You're at the recipe page.")
    all_recipes_name = Menu.objects.order_by('recipe_name')
    context = {
        'recipes_name': all_recipes_name,
    }
    template = loader.get_template('mywebsite/index.html')
    return HttpResponse(template.render(context, request))
#
# class IndexView(generic.ListView):
#     template_name = 'mywebsite/index.html'
#     context_object_name = 'recipes_name'
#
#     def get_queryset(self):
#         return Menu.objects.order_by('recipe_name')

class MenuDetailView(generic.DetailView):
    context_object_name = 'menu'
    queryset = Menu.objects.all()
    template_name = 'mywebsite/detail.html'

    # def get_queryset(self):
    #     return self.model


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username, password)
    context = 'Don\' know'
    if user is not None:
        login(request, user)
        context = 'User logged in'
    else:
        context = 'User not found'
    template = loader.get_template('mywebsite/login.html')
    return HttpResponse(template.render(context, request))
