from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.MenuDetailView.as_view(), name='menu-detail')
    # path('login', LoginView.as_view(), name='login')
]
