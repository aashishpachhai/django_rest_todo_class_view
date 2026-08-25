from django.urls import path
from . import views
urlpatterns=[
    path('todo/', views.Todos.as_view()),
    path('todo/<int:id>',views.TodoDetail.as_view())
]