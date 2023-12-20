from django.urls import path
from.import views
app_name='seller'


urlpatterns=[
    path('',views.Homes ,name="homes"),
    path('logins/',views.Logins,name="logins"),
    path('signups/',views.Signups,name="signups"),
    path('addproduct/',views.Addproduct,name="addproduct"),
    path('viewproduct/',views.Viewproduct,name="viewproduct"),
    path('delete//<int:pk>/',views.Delete,name="delete")
]