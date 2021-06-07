
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required (login_url='/accounts/login/')
def index(request):
    products = Product.objects.all()
    categories = Category.get_categories()
    title = "Home"

    return render(request, 'index.html', {'products':products, "title":title, 'categories':categories})


@login_required(login_url='/accounts/login/')
def profile(request, username):

    return render(request, 'profile.html')


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

    return render(request, 'update_profile.html', {'user_form': user_form, 'prof_form': prof_form})

@login_required(login_url='/accounts/login/')
def category(request, category):
    products = Product.filter_by_category(category)
    print(products)
    title = "By Category"
    return render(request, 'category.html', {'products': products, "title":title})


def product(request, id):
    product = Product.objects.get(id=id)
    current_user = request.user
    feedbacks = Feedback.objects.filter(product=product)
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
    
    return render(request, 'product.html', {'product': product, 'form': form, 'feedbacks':feedbacks})


@login_required(login_url='/accounts/login/')
def search(request):
    if request.method == 'GET':
        name = request.GET.get("name")
        results = Product.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        
        return render(request, 'results.html', {'results':results, 'message': message})
    else:
        message = "You haven't searched for any product"
    return render(request, 'results.html', {'message': message})
