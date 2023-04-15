from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('adoptapitbull/', views.adoptapitbull, name = 'adoptapitbull'),
    path('adopt/', views.adopt, name = 'adopt'),
    path('adoption-process/', views.adoptionprocess, name = 'adoption-process'),
    path('training/', views.training, name = 'training'),
    path('pit-bull-faq/', views.pitbullfaq, name = 'pit-bull-faq'),
    path('resources/', views.resources, name = 'resources'),
    path('foster/', views.foster, name = 'foster'),
    path('contact/', views.contact, name = 'contact'),
    path('events/', views.events, name = 'events'),
    path('volunteer/', views.volunteer, name = 'volunteer'),
    path('store/', views.store, name = 'store'),
    path('alumni/', views.alumni, name = 'alumni'),
    path('donate/', views.donate, name = 'donate'),
]
