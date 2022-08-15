from . import views
from django.urls import path

app_name='food'
urlpatterns = [
    #food/
    path('',views.IndexClassView.as_view(),name='index'),
    #food/item
    path('item/',views.item,name='item'),
    #food/id
    path('<int:pk>/',views.FoodDetails.as_view(),name="details"),
    #adding items
    path('add',views.AddItem.as_view(),name='add_item'),
    #edit items
    path('update/<int:id>/',views.update_item,name='update'),
    #delete items
    path('delete/<int:id>/',views.delete_item,name='delete_item'),

]
