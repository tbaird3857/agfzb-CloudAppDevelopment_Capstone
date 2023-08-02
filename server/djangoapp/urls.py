from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.index, name='index'),
    
    # path for about view
    path('about/', views.about, name='about'),

    # path for contact us view
    path('contact/', views.contact, name='contact'),
    # path for registration
    path('signup/', views.registration_request, name='signup'),
    # path for login
    path('login/', auth_views.LoginView.as_view(template_name='djangoapp/login.html'), name='login'),
    # path for logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view


    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)