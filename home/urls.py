from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('blog.urls')), # this directs to Read view of blog app
    # below paths call corresponding views in views.py oh home app
    path('authors/', views.Authors, name='authors'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
]
