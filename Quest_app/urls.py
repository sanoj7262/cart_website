
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('card_details',views.card_details,name="card_details"),
     path('pre_card_details',views.pre_card_details,name="pre_card_details"),
     path('delete_record/<id>',views.delete_record,name="delete_record"),
    path('update_record/<id>',views.update_record,name="update_record"),
     path('update_record_2/<id>',views.update_record_2,name="update_record_2"),
    path('collections',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
]
