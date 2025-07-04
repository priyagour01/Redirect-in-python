from django.shortcuts import render

# Create your views here.
def landingpage(req):
    return render(req,'landing.html')

def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def register(req):
    return render(req,'register.html')

def login(req):
    return render(req,'login.html')

def registerdata(req):
    print("hello.....")
    print(req.method)
    print(req.POST)
    print(req.FILES)
    return render(req,'base.html',{'register':'register'})


def nav(request):
    return render(request,'nav.html')

def shop(request):
    return render(request,'shop.html')