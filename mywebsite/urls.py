from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='index'),
    url('<int:pk>/', views.MenuDetailView.as_view(), name='menu-detail')
    # path('login', LoginView.as_view(), name='login')
]
