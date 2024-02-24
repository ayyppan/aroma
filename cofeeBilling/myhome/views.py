from django.shortcuts import render
from myhome.models import Part, Service_type, Service_price
from . import forms
from myhome.forms import UserProfileInfoForm, UserForm
from django.http import HttpResponseRedirect, HttpResponse 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    # return HttpResponse('Welcome to my Billing System!')
    # Service_type_list = Service_type.objects.order_by('part_number')

    # my_dict = {'service_entry':Service_type_list}

    my_dict = {'GSTIN_NO':'000001',
        'PO_NO':'01',
        'PO_DATE':'18-02-2024',
        'INVOICE_YEAR':'24-25',
        'INVOICE_SEQ':'0101',
        'INVOICE_DATE':'18-02-2024',
        'STATE':'KARNATAKA',
        'STATE_CODE':'29',
        'Billed_STATE':'TAMIL NADU',
        'CONTACT_PERSON':'Mr. Surendar',
        'ORG_NAME':'Aromatic coffe',
        'ADDR1':'ADDRESS 1',
        'ADDR2':'ADDRESS 2',
        'ADDR3':'KARNATAKA',
        'ADDR4':'560 017',
        'ACCOUNT_BANK':'UNION BANK',
        'ACCOUNT_BRANCH':'SANJAI NAGAR',
        'ACCOUNT_NAME':'AROMATIC COFFEE',
        'ACCOUNT_NO':'510101001398813',
        'ACCOUNT_IFSC':'UBIN0911739',
        'GSTIN_NUM':'29AAFCD0915M1ZH',
        'ITEM1':'RENTAL CHARGES ON MACHINE',
        'HSNACS1':'997319',
        'QTY1':'2',
        'UNIT_TYPE':'MC',
        'ITEM1_RATE':'2000',
        'ITEM1_TAX_VALUABLE':'4000',
        'ITEM1_CGST_RATE':'',
        'ITEM1_CGST_AMOUNT':'',
        'ITEM1_SGST_RATE':'',
        'ITEM1_SGST_AMOUNT':'',
        'ITEM1_IGST_RATE':'18%',
        'ITEM1_IGST_AMOUNT':'720',
        'ITEM1_TOTAL':'4720',
        'DC_NO':'Dc 001,63',
        'TOTAL_WITHOUT_TAX':'4000',
        'CGST_TOTAL':'0',
        'SGST_TOTAL':'0',
        'IGST_TOTAL':'720',
        'TOTAL_TAX':'720',
        'TOTAL_WITH_TAX':'4720',
    }
    return render(request,'myhome/index.html',context=my_dict)


########################## login - logout 
@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'myhome/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered
                   })

# create login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
        else:
            print("Some one try to login and failed!!")
            print("Username: {} and  Password{}".format(username,password))
            return HttpResponse("Invalid request posted")
    else:
        return render(request,'myhome/login.html',{})


##########################

def services(request):
    # return HttpResponse('Welcome to my Billing System!')
    Service_type_list = Service_type.objects.order_by('part_number')

    my_dict = {'service_entry':Service_type_list}
    return render(request,'myhome/serviced_entry_list.html',context=my_dict)

def prices(request):
    # return HttpResponse('Welcome to my Billing System!')
    Service_price_list = Service_price.objects.ordered

    my_dict = {'service_price':Service_price_list}
    return render(request,'myhome/serviced_entry_list.html',context=my_dict)


def form_customer_view(request):
    form_customer = forms.FormName()

    if request.method == "POST":
        form_customer = forms.FormName(request.POST)
        if form_customer.is_valid():
            print("Company Name: " + form.cleaned_data['Company_Name'])
            print("Address Line1: " + form.cleaned_data['Company_addr1'])
            print("Address Line2: " + form.cleaned_data['Company_addr2'])
            print("Address Line3: " + form.cleaned_data['Company_addr3'])
            print("Address Line4: " + form.cleaned_data['Company_addr4'])



def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            
            # print("Company Name: " + form.cleaned_data['Company_Name'])
            # print("Address Line1: " + form.cleaned_data['Company_addr1'])
            # print("Address Line2: " + form.cleaned_data['Company_addr2'])
            # print("Address Line3: " + form.cleaned_data['Company_addr3'])
            # print("Address Line4: " + form.cleaned_data['Company_addr4'])
            print("Service Name: " + form.cleaned_data['Service_name'])
            print("Quantity: " + str(form.cleaned_data['Quantity']))

            Service_type_list = Service_type.objects.order_by('part_number')
            my_dict = {'service_entry':Service_type_list}

            Service_price_list = Service_price.objects.order_by('Serv_price')
            my_dict = {'service_entry':Service_price_list}
            item_unit_price = 0 
            item_price = 0
            item_cgst_percent = 0
            item_cgst_amount = 0
            item_sgst_percent = 0
            item_sgst_amount = 0

            for serv in Service_price_list:
                # print (serv.Serv_price)
                # print (form.cleaned_data['Service_name'], str(serv.Serv_name)) 
                if str(serv.Serv_name) == form.cleaned_data['Service_name']:
                    item_unit_price = serv.Serv_price
                    item_price = int(round(item_unit_price * form.cleaned_data['Quantity'],0))
            for servT in Service_type_list:
                if str(servT.service_name) == form.cleaned_data['Service_name']:                 
                    item_cgst_percent = servT.cgst_val
                    item_cgst_amount = int(round((item_cgst_percent / 100) * item_price,0))
                    item_sgst_percent = servT.sgst_val
                    item_sgst_amount = int(round((item_sgst_percent / 100) * item_price,0))
            print (f"Unit Price {item_unit_price} Item Price: {item_price}; cgst: {item_cgst_percent}; cgst Amt: {item_cgst_amount}; sgst: {item_sgst_percent}; sgst Amt: {item_sgst_amount}")

    return render(request,'myhome/form_page.html',{'form':form})
