from django.shortcuts import render,redirect,get_object_or_404
from website.forms import Contacfrom
from website.models import Banner,Category,Brand,Product,cart
from django.db.models import Q

# Create your views here.,

def index(request):
    banner = Banner.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    product = Product.objects.all()
    
    context = {
        'banner' : banner,
        'category' : category,
        'brand' : brand,
        'product' : product
    }

    return render(request,'website/index.html',context)

def about(request):
    return render(request,'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = Contacfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Contacfrom()
    return render(request,'website/contact.html',{'form':form})

def pro_deta(request,pk):

    pro = Product.objects.get(pk=pk)
    related_produtd = Product.objects.filter(category=pro.category).exclude(id=pro.pk).order_by('?')[:11]
    context = {
        'pro':pro,
        'related_produtd' : related_produtd, 
    }
    return render(request,'website/product.html',context)

# def product_search(request):
#     query = request.GET['q']
#     lookup = (
#         Q(name__icontains=query) |
#         Q(category__name__icontains=query) | 
#         Q(brand__name__icontains=query)
#         )
#     search_product = Product.objects.filter(lookup)

#     context = {
#         'search_product': search_product
#     }
#     return render(request,'website/product_search.html',context)


def categories_product(request,pk):
    filtering = Category.objects.get(pk=pk)  
    product_filter= Product.objects.filter(category=filtering.id)
    return render(request,'website/categories_product.html',{'product_filter':product_filter})

def product_search(request):
    query = request.GET.get('q')  # Safely fetch the search query
    if query:
        lookup = (
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |  # Assuming 'category' is a ForeignKey to a model with a 'name' field
            Q(brand__name__icontains=query)       # Assuming 'brand' is a ForeignKey to a model with a 'name' field
        )
        search_product = Product.objects.filter(lookup)
    else:
        search_product = Product.objects.none()  # Return empty queryset if no query is provided

    context = {
        'search_product': search_product
    }
    return render(request, 'website/product_search.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('contact')
  