from django.shortcuts import render,HttpResponse
from .models import product,Contact,Orders,orderstatus
# Create your views here.
import json,datetime
def index(request):
    cat=(product.objects.values('category','id'))

    cats={item['category'] for item in cat}
    ap=[]
    for c in cats:
        pr=product.objects.filter(category=c)
        ln=len(pr)
        mul=ln//4
        if mul*4==ln:
            no_of_slide=mul
        else:
            no_of_slide=mul+1
        flag=0
        ap.append([pr,range(1,no_of_slide),no_of_slide,[0]])

    prodt={'ap':ap}

    return render(request,'shop/index.html',prodt)

def about(request):
    return render(request,'shop/about.html')

def contact(request):

    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        connect=True
        return render(request,'shop/contact.html',{'c':connect})
    
    return render(request,'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderid=request.POST.get('orderid','')
        email=request.POST.get('email','')
        # return HttpResponse(f"{orderid} and {email}")
        
        try:
            res=Orders.objects.filter(o_id=orderid,email=email)

            if len(res)!=0:
                update=orderstatus.objects.filter(orderid=orderid)
                updates=[]
                for i in update:

                    st="{0}/{1}/{2}".format(i.timestamp.day,i.timestamp.month,i.timestamp.year)
                    updates.append({'text':i.updatedesc.upper(),'time':st})

                respose=json.dumps([updates,res[0].items_json],default=str)
                return HttpResponse(respose)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def productview(request,myid):
    pr=product.objects.filter(id=myid)
    return render(request,'shop/product.html',{'prod':pr[0]})

def checkout(request):
    thank=False
    if request.method=="POST":
        itemjson=request.POST.get('itemjson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address1','') + " " + request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zipcode','')

        order=Orders(items_json=itemjson,name=name,email=email,phone=phone,address=address,city=city,state=state,zipcode=zipcode)
        order.save()
        thank=True
        id=order.o_id
        track=orderstatus(orderid=id,updatedesc="Your Order has been placed")
        track.save()
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})

    return render(request,'shop/checkout.html')
