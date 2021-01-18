from django.urls import path
from . import views

urlpatterns =[
    path('',views.list_todo_items),
    path('insert',views.insert,name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete,name='delete_todo_item'),
]

