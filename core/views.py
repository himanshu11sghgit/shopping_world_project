from math import fabs
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *
from .forms import *



class Signup(View):
    def get(self, request):
        form = SignupForm()
        context = {'form': form}
        return render(request, 'core/signup.html', context)

    def post(self, request):
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is successfully created.')
            return HttpResponseRedirect('/accounts/login/')
        else:
            context = {'form': form}
            return render(request, 'core/signup.html', context)


class Login(LoginView):
    template_name = 'core/login.html'
    authentication_form = LoginForm



@method_decorator(login_required, name="dispatch")
class PasswordChange(PasswordChangeView):
    template_name = 'core/password_change.html'
    form_class = CustomPasswordChangeForm
    success_url = '/password_change/done/'

@method_decorator(login_required, name="dispatch")
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'core/password_change_done.html'

@method_decorator(login_required, name="dispatch")
class PasswordReset(PasswordResetView):
    template_name = 'core/password_reset.html'
    form_class = CustomPasswordResetForm

@method_decorator(login_required, name="dispatch")
class PasswordResetDone(PasswordResetDoneView):
    template_name = 'core/password_reset_done.html'


@method_decorator(login_required, name="dispatch")
class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'core/password_reset_confirm.html'
    form_class = CustomSetPasswordForm


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'core/password_reset_complete.html'


@method_decorator(login_required, name="dispatch")
class Logout(LogoutView):
    next_page = 'login'


@method_decorator(login_required, name="dispatch")
class Profile(View):
    def get(self, request):
        form = CustomerProfileForm
        context = {
            'form': form,
            'active': 'btn-primary'
        }
        return render(request, 'core/profile.html', context)

    def post(self, request):
        form = CustomerProfileForm(data=request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            pincode = form.cleaned_data['pincode']
            state = form.cleaned_data['state']
            customer = Customer(user=user, name=name, locality=locality, city=city, pincode=pincode, state=state)
            customer.save()
            messages.success(request, 'Your address is successfully added!!')

        context = {
            'form': form,
            'active': 'btn-primary'
        }
        return render(request, 'core/profile.html', context)


@method_decorator(login_required, name="dispatch")
class Address(View):
    def get(self, request):
        addresses = Customer.objects.filter(user=request.user)
        context = {
            'addresses': addresses,
            'active': 'btn-primary',
        }
        return render(request, 'core/address.html', context)


class Home(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')

        context = {
            'topwears': topwears,
            'bottomwears': bottomwears,
            'mobiles': mobiles,
            'laptops': laptops
        }
        return render(request, 'core/home.html', context)



class ProductDetails(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
           item_already_in_cart  = Cart.objects.filter(Q(user=request.user) & Q(product=product)).exists()

        context = {
            'product': product,
            'item_already_in_cart': item_already_in_cart
        }
        return render(request, 'core/product_detail.html', context)


@method_decorator(login_required, name="dispatch")
class AddToCart(View):
    def get(self, request):
        user = request.user
        product_id = request.GET.get('product_id')
        print(product_id)
        product = Product.objects.get(id=product_id)
        cart = Cart(user=user, product=product)
        cart.save()
        return redirect('/show_cart/')


@method_decorator(login_required, name="dispatch")
class ShowCart(View):
    def get(self, request):
        if request.user.is_authenticated:
            items = Cart.objects.filter(user=request.user)
            
            amount = 0.0
            shipping = 500.0
            total_amount = 0.0
            product_data = [pd for pd in Cart.objects.all() if pd.user == request.user]
            print(product_data)

            if product_data:
                for pd in product_data:
                    product_amount = pd.product.discounted_price * pd.quantity
                    amount += product_amount
                total_amount = amount + shipping

                context = {
                    'items': items,
                    'amount': amount,
                    'shipping': shipping,
                    'total_amount': total_amount,
                    }
                return render(request, 'core/show_cart.html', context)
            else:
                return render(request, 'core/empty_cart.html')

        else:
            return redirect('/login/')

@method_decorator(login_required, name="dispatch")
class PlusCart(View):
    def get(self, request):
        product_id = request.GET.get('product_id')
        item = Cart.objects.get(Q(user=request.user) & Q(product=product_id))
        item.quantity += 1
        item.save()

        amount = 0.0
        shipping = 500.0
        total_amount = 0.0
        product_data = [pd for pd in Cart.objects.all() if pd.user == request.user]

        if product_data:
            for pd in product_data:
                product_amount = pd.product.discounted_price * pd.quantity
                amount += product_amount
            total_amount = amount + shipping

        context = {
            'quantity': item.quantity,
            'amount': amount,
            'shipping': shipping,
            'total_amount': total_amount,
            }
        return JsonResponse(context)

@method_decorator(login_required, name="dispatch")
class MinusCart(View):
    def get(self, request):
        product_id = request.GET.get('product_id')
        item = Cart.objects.get(Q(user=request.user) & Q(product=product_id))
        item.quantity -= 1
        item.save()

        amount = 0.0
        shipping = 500.0
        total_amount = 0.0
        product_data = [pd for pd in Cart.objects.all() if pd.user == request.user]

        if product_data:
            for pd in product_data:
                product_amount = pd.product.discounted_price * pd.quantity
                amount += product_amount
            total_amount = amount + shipping

        context = {
            'quantity': item.quantity,
            'amount': amount,
            'shipping': shipping,
            'total_amount': total_amount,
            }
        return JsonResponse(context)

@method_decorator(login_required, name="dispatch")
class RemoveCart(View):
    def get(self, request):
        product_id = request.GET.get('product_id')
        item = Cart.objects.get(Q(user=request.user) & Q(product=product_id))
        item.delete()

        amount = 0.0
        shipping = 500.0
        total_amount = 0.0
        product_data = [pd for pd in Cart.objects.all() if pd.user == request.user]

        if product_data:
            for pd in product_data:
                product_amount = pd.product.discounted_price * pd.quantity
                amount += product_amount
            total_amount = amount + shipping

        context = {
            'amount': amount,
            'shipping': shipping,
            'total_amount': total_amount,
            }
        print(context)
        return JsonResponse(context)

        
@method_decorator(login_required, name="dispatch")
class Checkout(View):
    def get(self, request):
        addresses = Customer.objects.filter(user=request.user)
        items = Cart.objects.filter(user=request.user)

        amount = 0.0
        shipping = 500.0
        total_amount = 0.0
        product_data = [pd for pd in Cart.objects.all() if pd.user == request.user]

        if product_data:
            for pd in product_data:
                product_amount = pd.product.discounted_price * pd.quantity
                amount += product_amount
            total_amount = amount + shipping

        context = {
            'addresses': addresses,
            'items': items,
            'amount': amount,
            'shipping': shipping,
            'total_amount': total_amount,
            }
        print(context)
        return render(request, 'core/checkout.html', context)

@method_decorator(login_required, name="dispatch")
class PaymentDone(View):
    def get(self, request):
        customer_id = request.GET.get('customer_id')
        customer = Customer.objects.get(id=customer_id)
        items = Cart.objects.filter(user=request.user)

        for item in items:
            order = OrderPlaced(user=request.user, customer=customer, product=item.product, quantity=item.quantity)
            order.save()
            item.delete()
        
        return redirect('/orders/')


@method_decorator(login_required, name="dispatch")
class Orders(View):
    def get(self, request):
        orders = OrderPlaced.objects.filter(user=request.user)
        context = {'orders': orders}
        return render(request, 'core/orders.html', context)


def topwears(request, data=None):
    topwears = Product.objects.filter(category='TW')
    if data is None:
        items = topwears

    elif data == 'Below': 
        items = topwears.filter(discounted_price__lt=2000)
    elif data == 'Above': 
        items = topwears.filter(discounted_price__gt=2000)
        
    else:
        items = topwears.filter(brand=data)

    context = {'items': items}
    return render(request, 'core/topwears.html', context)
    

def bottomwears(request, data=None):
    bottomwears = Product.objects.filter(category='BW')
    if data is None:
        items = bottomwears

    elif data == 'Below': 
        items = bottomwears.filter(discounted_price__lt=2000)
    elif data == 'Above': 
        items = bottomwears.filter(discounted_price__gt=2000)
        
    else:
        items = bottomwears.filter(brand=data)

    context = {'items': items}
    return render(request, 'core/bottomwears.html', context)
    

def mobiles(request, data=None):
    mobiles = Product.objects.filter(category='M')
    if data is None:
        items = mobiles

    elif data == 'Below': 
        items = mobiles.filter(discounted_price__lt=10000)
    elif data == 'Above': 
        items = mobiles.filter(discounted_price__gt=10000)
        
    else:
        items = mobiles.filter(brand=data)

    context = {'items': items}
    return render(request, 'core/mobiles.html', context)
    

def laptops(request, data=None):
    laptops = Product.objects.filter(category='L')
    if data is None:
        items = laptops

    elif data == 'Below': 
        items = laptops.filter(discounted_price__lt=60000)
    elif data == 'Above': 
        items = laptops.filter(discounted_price__gt=60000)
        
    else:
        items = laptops.filter(brand=data)

    context = {'items': items}
    return render(request, 'core/laptops.html', context)
    




