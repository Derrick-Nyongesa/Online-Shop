
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse,Http404,HttpResponseRedirect, request
from .email import send_welcome_email
from django.contrib import messages
from .models import Cart, Product, Profile, Feedback

# Create your views here.
@login_required (login_url='/accounts/login/')
def index(request):
    products = Product.objects.all()
    categories = Category.get_categories()
    title = "Home"
    cart_items = Cart.get_user_cart(request.user)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient = SubscriptionRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('homePage')
    else:
        form = SubscriptionForm()

    return render(request, 'index.html', {'products':products, "title":title, 'cart_items':cart_items,'categories':categories,'form':form})


@login_required(login_url='/accounts/login/')
def profile(request, username):
    cart_items = Cart.get_user_cart(request.user, )

    return render(request, 'profile.html',{'cart_items':cart_items})


@login_required(login_url='/accounts/login/')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UserForm(instance=request.user)
        prof_form = ProfileForm(instance=request.user.profile)
        cart_items = Cart.get_user_cart(request.user)

    return render(request, 'update_profile.html', {'user_form': user_form, 'prof_form': prof_form, 'cart_items':cart_items})

@login_required(login_url='/accounts/login/')
def category(request, category):
    products = Product.filter_by_category(category)
    print(products)
    title = "By Category"
    cart_items = Cart.get_user_cart(request.user)
    return render(request, 'category.html', {'products': products, "title":title, 'cart_items':cart_items,})


def product(request, id):
    product = Product.objects.get(id=id)
    current_user = request.user
    in_cart = Cart.in_cart(product, current_user)
    feedbacks = Feedback.objects.filter(product=product)
    cart_items = Cart.get_user_cart(request.user)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            p_form = form.save(commit=False)
            p_form.product = product
            p_form.user = current_user
            p_form.save()
            return redirect('product', product.id)
    else:
        form = FeedbackForm()
    
    return render(request, 'product.html', {'product': product, 'form': form, 'feedbacks':feedbacks, 'cart_items':cart_items, 'in_cart': in_cart})


@login_required(login_url='/accounts/login/')
def search(request):
    if request.method == 'GET':
        name = request.GET.get("name")
        results = Product.objects.filter(name__icontains=name).all()
        print(results)
        cart_items = Cart.get_user_cart(request.user)
        message = f'found results'
        
        return render(request, 'results.html', {'results':results, 'message': message, 'cart_items':cart_items})
    else:
        message = "You haven't searched for any product"
    return render(request, 'results.html', {'message': message})



@login_required(login_url='/accounts/login/')
def cart(request):
    cart_items = Cart.get_user_cart(request.user)
    
    total=0
    for product in cart_items:
        total = total + product.product.price

    return render(request, "cart.html", {'cart_items':cart_items,'total':total})

    

@login_required(login_url='/accounts/login/')
def add(request, id):
    product = Product.objects.get(id=id)
    Cart.add_product(product, request.user)
    return redirect("product", id)

@login_required(login_url='/accounts/login/')
def remove(request, id):
    product = Product.objects.get(id=id)
    Cart.remove_product(product, request.user)
    return redirect("cart")


@login_required(login_url='/accounts/login/')
def payment(request):
    current_user = request.user
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            card_number = form.cleaned_data['card_number']
            #form = form.save(commit=False)
            #form.user = current_user
            customers = Payment(first_name = first_name, last_name = last_name, email =email, card_number=card_number)
            customers.save()
            return redirect('success')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})


@login_required(login_url='/accounts/login/')
def success(request):

    return render(request, 'success.html')
