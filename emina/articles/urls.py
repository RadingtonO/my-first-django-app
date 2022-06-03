from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', views.main_list, name='main'),
    path('category:<int:category_id>/', views.detail_articles, name='category'),
    path('articles:<int:article_id>/results/', views.results_articles, name='results'),
    path('register/', MyRegisterFormView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
