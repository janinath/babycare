from django.urls import path
from.import views
from .views import SellerProductListView
app_name='customers'


urlpatterns=[
    path('',views.Home ,name="home"),
    path('login/',views.Login,name="login"),
    path('signup/',views.Signup,name="signup"),
    path('dashboard/',views.Dashboard,name="dashboard"),
    path('seller_products/', SellerProductListView.as_view(), name='seller_products'),
    path('searchproduct/',views.Searchproduct,name="searchproduct"),
    path('cart_/',views.Cart_,name="cart"),
    path('viewpdt/<int:product_id>',views.Viewpdt,name="viewpdt"),
    path('buy/<int:id>',views.Buy,name="buy"),
    path('pay',views.Pay,name="pay"),
    path('deletecartitem//<int:pk>/',views.DeleteCartItem,name="deletecartitem"),
    path('razorpay_payment/', views.razorpay_payment, name='razorpay_payment'),
    path('logout/',views.Logout,name="logout")
    
    
]

