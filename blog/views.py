
from django.shortcuts import render,redirect
from blog.models import Post,Category,Tag,Contact,Author_name
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def INDEX(request):
    popular_post=Post.objects.filter(section='Popular',status=1).order_by('-id')[0:4]
    recent_post=Post.objects.filter(section='Recent',status=1).order_by('-id')[0:4]
    main_post=Post.objects.filter(main_post=True,status=1)[0:1]
    editors_pick=Post.objects.filter(section='Editors_Pick',status=1).order_by('-id')
    trending_post=Post.objects.filter(section='Trending',status=1).order_by('-id')
    Inspiration=Post.objects.filter(section='Inspiration',status=1).order_by('-id')[0:2]
    Latest_Posts=Post.objects.filter(section='Latest_Posts',status=1).order_by('-id')[0:4]
    
    category=Category.objects.all()
    tag=Tag.objects.all()
    
    context={
        'popular_post':popular_post,
        'recent_post':recent_post,
        'main_post':main_post,
        'editors_pick':editors_pick,
        'trending_post':trending_post,
        'Inspiration':Inspiration,
        'Latest_Posts':Latest_Posts,
        'category':category,
        'tag':tag,
    }
    return render(request, "main/index.html",context)


def ABOUT(request):
    return render(request, "main/about.html")

def CONTACT(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact_views=Contact(username=username,email=email,subject=subject,message=message)
        contact_views.save()
        return redirect("/")
        
    return render(request, "main/contact.html")


def BLOG_SINGLE(request,slug):

    single_details = Post.objects.get(slug=slug)

    
    popular_post=Post.objects.filter(section='Popular').order_by('id') 
    trending_post=Post.objects.filter(section='Trending',status=1).order_by('-id')
    category=Category.objects.all()
    
   
    context={
        'single_details':single_details,
        
        'popular_post':popular_post,
        'trending_post':trending_post,
        'category':category, 
        
    }
    return render(request, "main/blog_single.html",context)

#================search==========================
def SEARCH(request):
    search_key=request.GET.get('search', None)
    # tag=Tag.objects.order_by('date') tag  dia jadi search dite hay tai dite parven
    if search_key:
        blogs=Post.objects.filter(
            Q(title__icontains=search_key) | 
            Q(author__icontains=search_key)|
            Q(tag__name__icontains=search_key) |
            Q(category__name__icontains=search_key)).distinct()
        context={
            'blogs':blogs,
   
            'search_key':search_key
        }
        return render(request, 'main/search.html', context)
    else:
        blogs=Post.objects.order_by('date')
        context={
            'blogs':blogs
        }
        return render(request, 'main/search.html', context)
        



# def SEARCH(request):
#     search=request.GET.get('search')
#     title=Post.objects.filter(title__icontains=search)
#     context={
#         'title':title, 
#     }
#     return render(request, 'main/search.html', context)

#================search==========================


def ALL_BLOGS(request):
    blogs=Post.objects.all()
    category=Category.objects.all()
    tag=Tag.objects.all()
    
    
    
    CATID=request.GET.get('category')# HTML link  name'categories'
    AUTHOR=request.GET.get('author')# HTML link  name'categories'
    if CATID:
        blogs=Post.objects.filter(category=CATID)# models forenkey name 'categories'
    elif AUTHOR:
        blogs=Post.objects.filter(author=AUTHOR)# models forenkey name 'categories'
    else:
        blogs=Post.objects.filter()
        
    context={
        'blogs':blogs,
        'category':category,
        'tag':tag,
        
        
        
    }
    return render(request, 'main/all_blogs.html',context)

            
#Authentication start============================================================
def handleRegister(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass12')
        
        register_views=User.objects.create_user(username,email,pass1)
        register_views.first_name=first_name
        register_views.last_name=last_name
        register_views.save()
        return redirect('register')
    
    return render(request, 'authentication/auth.html')

def handleLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('login')
         
    return render(request, 'authentication/auth.html')

def handleLogout(request):
    logout(request)
    return redirect('/')
#Authentication end============================================================

