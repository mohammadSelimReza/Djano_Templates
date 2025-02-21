from django.urls import path
from . import views 
urlpatterns = [
    path("",views.home,name='homepage'),
    path("create/item/",views.add_item,name='add_item'),
    path("update/item/<int:pk>",views.update_item,name='update_item'),
    path("delete/item/<int:pk>",views.delete_item,name='delete_item'),
]
