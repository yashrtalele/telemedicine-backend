from pathlib import Path
from . import views
from django.urls import path
from api.views import ArticleList

urlpatterns = [
    path('article', ArticleList.as_view()),   
    path('article/<int:id>', views.recommendations),
    path('predict', views.prediction)
]