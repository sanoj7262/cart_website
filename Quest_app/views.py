

from multiprocessing import context
from django.shortcuts import render,redirect

from Quest_app.form import CustomUserForm,paymentform
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,'Quest_app/index.html')
    
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration successfull you can login Now...")
            return redirect('/login')

    return render(request,'Quest_app/register.html',{'form':form})


def login_page(request):
    if request.method =='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
          login(request,user)
          messages.success(request,"loged in successfully")
          return redirect("/")
        else:
          messages.error(request,"Invalid User Name or password")
          return redirect('/login')
    return render(request,'Quest_app/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully")
        return redirect("/")

def collections(request):
    categories=category.objects.filter(status=0)
    return render(request,"Quest_app/collections.html",{"categories":categories})

def collectionsview(request,name):
    if(category.objects.filter(name=name,status=0)):
        products=product.objects.filter(category__name=name)
        return render(request,"Quest_app/products/index.html",{"products_1":products})
    else:
        messages.warning(request,"No such category Found")
        return redirect('collections')

def card_details(request):
    form=paymentform()
    if request.method=='POST':
        form=paymentform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Card details successfull added")
            return redirect('/pre_card_details')

    return render(request,'Quest_app/card_details.html',{'form':form})
    # return render(request,'Quest_app/card_details.html')      

def pre_card_details(request):
    data=Card_details.objects.all()
    return render(request,'Quest_app/pre_card_details.html',{'pre_card_details':data})



def delete_record(request,id):
    trash=Card_details.objects.get(id=id)
    trash.delete()
    return redirect('/pre_card_details')



def update_record(request,id):
    modify=Card_details.objects.get(id=id)
    modify_2=Card_details.objects.all()
    context={
        'modify':modify,
        'modify_2':modify_2
    }

    # if request.method=='POST':
    #     form=paymentform(request.POST,instance=modify)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"Updated successfully ")
    #         return redirect('/pre_card_details')
    return render(request,'Quest_app/update.html',context)


def update_record_2(request,id):
    item=Card_details.objects.get(id=id)
    
    item.Card_Number=request.POST['card_number']
    item.Expiry_details=request.POST['expiry']
    item.Cardholder_Name=request.POST['holdername']
    item.save()
    messages.success(request,"Updated successfully ")
    return redirect('/pre_card_details')






 



