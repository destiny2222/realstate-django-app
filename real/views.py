from django.views.generic import ListView,DetailView,CreateView,TemplateView
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.http import   Http404,HttpResponse
from real.models import *
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import  UpdateView
from .choices import bedroom_choices, properity_type_choices ,bath_rooms_choices
from django.core.paginator import  Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required

user = get_user_model()
# Create your views here.

def homeview(request):
    property = Listing.objects.order_by('-list_date').all()[:6]
    find_location = Featured.objects.filter(is_active=True)[:6]
    blog = Post.objects.all()[:3]
    content = {
        'property':property, 
        'find_location':find_location,
        'properity_type_choices': properity_type_choices,
        'bedroom_choices': bedroom_choices,
        'bath_rooms_choices': bath_rooms_choices,
        'blog':blog,
        'values': request.POST

        }
    return render(request, 'index.html', content)




def AddProperity(request):
    form = PropertyForm()
    submitted = False
    if request.method == 'POST':
        if request.user.is_superuser:
            form = PropertyFormAdmin(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Property Added Successful')
                return redirect('index:my_property')
        else:
            form = PropertyForm(request.POST, request.FILES)
            if form.is_valid():
                list = form.save(commit=False)
                list.listing_user = request.user
                list.save()
                messages.success(request, 'Property Added Successful')
                return redirect('index:my_property')
    else:
        # just going to the page, not submitting
        if request.user.is_superuser:
            form = PropertyFormAdmin()
        else:
            form = PropertyForm()
            if 'submitted' in request.GET:
                submitted = True
            messages.error(request, form.errors)
    return render(request, 'property.html', {'form':form})  



# def EditView(request, slug):
#     post = Listing.objects.get(slug=slug) 
#     form = PropertyForm()
#     if request.method == "POST":
#         form = PropertyForm(instance=post,data=request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#             messages.success(request, f"Your Property Info has been updated")
#             return redirect("index:my_property")
#         else:
#             messages.success(request, form.errors)
#     context = {'form': form}
#     return render(request, 'account/property_edit.html', context)
    



class EditView(SuccessMessageMixin,UpdateView):
    model = Listing
    template_name = "account/property_edit.html"
    form_class = PropertyForm
    success_url = reverse_lazy('index:my_property')
    success_message = 'Your Property Info has been updated!!!!'
      


@login_required(login_url='indexurl:login') 
def del_listing(request, slug):
    # poster = Listing.objects.get(listing_user=request.user, slug=slug)
    poster = Listing.objects.get(slug=slug)
    poster.delete()
    messages.info(request, 'Successful Delete Property')
    return redirect('index:my_property')
    # return render(request, 'del_done.html') 


def ProperityView(request):
    pro_view = Listing.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(pro_view, 3)
    try:
        pro = paginator.page(page)
    except PageNotAnInteger:
        # if is not an integer, deliver the first page
        pro = paginator.page(1)
    except EmptyPage:
        # if the page is out of range deliver the last page
        pro = paginator.page(paginator.num_pages) 
    content = {'pro':pro,}
    return render(request, 'property-view.html', content)

def DetailsViews(request, slug):
    feature = Featured.objects.order_by('-list_date').all()[:4]
    admindetails = CustomUser.objects.filter(is_superuser=True)[:1]
    single = Listing.objects.filter(slug=slug)
    if single.exists():
        single = Listing.objects.get(slug=slug)
    else:
        return redirect("index:404")
    if request.method == 'POST':
        comment_form = ReviewForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.review = single
            new_comment.save()

        else:
            messages.error(request, comment_form.errors)
            comment_form = ReviewForm()
    else:
        comment_form = ReviewForm()         
    content = {'single':single, 'feature':feature,
                'comment_form': comment_form, 'superuser':admindetails}    
    return render(request, 'single-property.html', content)


def FeatureView(request):
    feaut = Featured.objects.all()
    paginator = Paginator(feaut, 3)
    page = request.GET.get('page')
    try:
        feaut = paginator.page(page)
    except PageNotAnInteger:
        # if is not an integer, deliver the first page
        feaut = paginator.page(1)
    except EmptyPage:
        # if the page is out of range deliver the last page
        feaut = paginator.page(paginator.num_pages) 
    content = {'feaut':feaut, 'page':page,}
    return render(request, 'featured.html', content)

def FeatureDetails(request, slug):
    feature = Featured.objects.order_by('-list_date').all()[:4]
    sing = Featured.objects.filter(slug=slug)
    if sing.exists():
        sing = Featured.objects.get(slug=slug)
    else:
        return redirect("index:404")          
    content = {'sing':sing, 'feature':feature,}    
    return render(request, 'featured-single.html', content)




def Error404(request):

    return render(request, '404.html')    


def AboutView(request):
    return render(request, 'about-us.html')


def blogview(request):
    post = Post.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(post, 3)
    try:
        post_blog = paginator.page(page)
    except PageNotAnInteger:
        # if is not an integer, deliver the first page
        post_blog = paginator.page(1)
    except EmptyPage:
        # if the page is out of range deliver the last page
        post_blog = paginator.page(paginator.num_pages) 
    content = {'post_blog':post_blog, 'page':page}
    return render(request, 'blog.html', content)

def postdetailview(request, slug):
    details = Post.objects.filter(slug=slug)
    recentpost = Post.objects.all().order_by('-id')[:4]
    if details.exists():
        details = Post.objects.get(slug=slug)
    else:
        return redirect("index:404")
    content = {'details':details, 'recentpost':recentpost}    
    return render(request, 'blog-detail.html', content)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # KEYWORDS
    
    if 'address' in request.POST:
        address = request.POST['address']
        if address:
            queryset_list = queryset_list.filter(address__icontains=address)

    # CITY
    if 'city' in request.POST:
        city = request.POST['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # STATE
    if 'state' in request.POST:
        state = request.POST['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # BEDROOMS
    if 'bedrooms' in request.POST:
        bedrooms = request.POST['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # BATHROOM
    if 'property_type' in request.POST:
        property_type = request.POST['property_type']
        if property_type:
            queryset_list = queryset_list.filter(property_type__lte=property_type)



    # PRICE
    if 'price' in request.POST:
        price = request.POST['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
    }

    return render(request, 'sarech.html', context)


def Contactview(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            sub = "Website Inquiry" 
            body = {
                'name': form.cleaned_data['name'], 
                'subject': form.cleaned_data['subject'], 
                'email': form.cleaned_data['email'], 
                'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())
        try:
            send_mail(sub, message, 'text33131@gmail.com', ['text33131@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect ("index:contact")
    form = ContactForm()
    return render(request, 'contact.html')

   


def Faq(request):

    return render(request, 'faq.html')