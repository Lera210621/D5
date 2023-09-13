from django.urls import path
# Импортируем созданное нами представление
from .views import ProductsList , ProductDetail, Search_List, PostCreate,Post_Update,Post_Delete, subscriptions
from .filters import ProductFilter
#from .views import upgrade_user



urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('news/', ProductsList.as_view(),name='product_list'),
   path('<int:pk>', ProductDetail.as_view(),name='product_detail'),
   path('news/search/', Search_List.as_view(),name='search_list'),
   path('news/create/', PostCreate.as_view(),name='product_create'),
   path('<int:pk>/update/',Post_Update.as_view(),name='product_update'),
   path('<int:pk>/delete/',Post_Delete.as_view(),name='product_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]
