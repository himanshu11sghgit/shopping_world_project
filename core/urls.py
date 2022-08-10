from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product_detail/<int:pk>/', views.ProductDetails.as_view(), name='product_detail'),

    path('add_to_cart/', views.AddToCart.as_view(), name='add_to_cart'),
    path('show_cart/', views.ShowCart.as_view(), name='show_cart'),
    path('plus_cart/', views.PlusCart.as_view(), name='plus_cart'),
    path('minus_cart/', views.MinusCart.as_view(), name='minus_cart'),
    path('remove_cart/', views.RemoveCart.as_view(), name='remove_cart'),
    path('orders/', views.Orders.as_view(), name='orders'),
    
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('payment_done/', views.PaymentDone.as_view(), name='payment_done'),


    path('topwears/', views.topwears, name='topwears'),
    path('topwears/<slug:data>/', views.topwears, name='topwears_data'),
    path('bottomwears/', views.bottomwears, name='bottomwears'),
    path('bottomwears/<slug:data>/', views.bottomwears, name='bottomwears_data'),
    path('mobile/', views.mobiles, name='mobiles'),
    path('mobile/<slug:data>/', views.mobiles, name='mobiles_data'),
    path('laptops/', views.laptops, name='laptops'),
    path('laptops/<slug:data>/', views.laptops, name='laptops_data'),

    path('profile/', views.Profile.as_view(), name='profile'),
    path('address/', views.Address.as_view(), name='address'),
    
    path('signup/', views.Signup.as_view(), name='signup'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('logout/', views.Logout.as_view(), name='logout'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
