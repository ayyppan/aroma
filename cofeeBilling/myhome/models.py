from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

# USER
class UserProfileInfo(models.Model):
    #create relationship oneToOne
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # additional info
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='media/profile_pics', blank=True)

    def __str__(self):
        return self.user.username
    

# Create your models here.
class Part(models.Model):
    part_num = models.CharField(max_length=8,unique=True)
    
    def __str__(self):
        return f"{self.part_num}"


class Service_type(models.Model):
    part_number = models.ForeignKey(Part,on_delete=models.CASCADE)
    hsn_code = models.CharField(max_length=20)
    service_name = models.CharField(max_length=100,unique=True)
    # service_unit_price = models.FloatField()
    cgst_val = models.FloatField()
    sgst_val = models.FloatField()
    igst_val = models.FloatField()

    def __str__(self):
        # return f"{self.part_number} ==> {self.hsn_code} ==> {self.service_name} ==> {self.cgst_val} ==> {self.sgst_val}"
        return f"{self.service_name}"

class Service_price(models.Model):
    Serv_name = models.ForeignKey(Service_type,on_delete=models.CASCADE, to_field='service_name')
    Serv_price = models.FloatField()
    # service_unit_price = models.FloatField()

    def __str__(self):
        return f"{self.Serv_name} ==> {self.Serv_price}"


class customer(models.Model):
    Cus_name = models.CharField(max_length=100,unique=True)
    Cus_DoorNo = models.FloatField(max_length=200)
    Cus_Street = models.FloatField(max_length=200)
    Cus_City = models.FloatField(max_length=100)
    Cus_Dist = models.FloatField(max_length=100)
    Cus_State = models.FloatField(max_length=100)
    Cus_Pin = models.FloatField(max_length=7)

    def __str__(self):
        return f"{self.Cus_name}\n{self.Cus_DoorNO}\n{self.Cus_Street}\n{self.Cus_City}\n{self.Cus_State}"

class Org_Bank(models.Model):
    Org_BankName = models.CharField(max_length=100)
    Org_Bnk_Branch = models.FloatField(max_length=100)
    Org_Ac_Name = models.FloatField(max_length=100)
    Org_Ac_No = models.FloatField(max_length=15)
    Org_Ac_Ifsc = models.FloatField(max_length=20)

    def __str__(self):
        return f"{self.Org_BankName}\n{self.Org_Bnk_Branch}\n{self.Org_Ac_Name}\n{self.Org_Ac_No}\n{self.Org_Ac_Ifsc}"

class Billing(models.Model):
    GSTIN_NO = models.CharField(max_length=25)
    PO_NO = models.CharField(max_length=25)
    PO_DATE = models.DateField()
    INVOICE_YEAR = models.CharField(max_length=10,default="ARO/24-25/")
    INVOICE_DATE = models.DateField()
    STATE = models.CharField(max_length=50)
    STATE_CODE = models.CharField(max_length=5,default='29')
    BILLED_STATE = models.CharField(max_length=50,default='KARNATAKA')
    CONTACT_PERSON = models.CharField(max_length=50, default='Mr./Mrs/Miss ')
    COMPANY_NAME = models.CharField(max_length=50)
    DOOR_NO = models.CharField(max_length=150)
    STREET = models.CharField(max_length=150)
    CITY = models.CharField(max_length=150)
    DIST = models.CharField(max_length=150)
    STATE = models.CharField(max_length=150, default='KARNATAKA')
    PIN = models.CharField(max_length=7)
    ACCOUNT_BANK = models.CharField(max_length=100,default='UNION  BANK')
    ACCOUNT_BRANCH = models.CharField(max_length=150,default='SANJAY NAGAR')
    ACCOUNT_NAME = models.CharField(max_length=150,default="AROMATIC COFFEE")
    ACCOUNT_NO = models.CharField(max_length=20,default='510101001398813')
    ACCOUNT_IFSC = models.CharField(max_length=15,default='UBIN0911739')
    GSTIN_NUM = models.CharField(max_length=25,default='SANJAY NAGAR')
    ITEM = models.CharField(max_length=150)
    HSNACS = models.CharField(max_length=15)
    QTY = models.IntegerField()
    UNIT_TYPE = models.CharField(max_length=10)
    UNIT_PRICE = models.FloatField()
    TAX_VALUABLE = models.FloatField()
    CGST_RATE = models.FloatField()
    CGST_AMOUNT = models.FloatField()
    SGST_RATE = models.FloatField()
    SGST_AMOUNT = models.FloatField()
    IGST_RATE = models.FloatField()
    IGST_AMOUNT = models.FloatField()
    TOTAL = models.FloatField()
    DC_NO = models.CharField(max_length=20)
    TOTAL_WITHOUT_TAX = models.FloatField()
    CGST_TOTAL = models.FloatField()
    SGST_TOTAL = models.FloatField()
    IGST_TOTAL = models.FloatField()
    TOTAL_TAX = models.FloatField()
    TOTAL_WITH_TAX = models.FloatField()


    def __str__(self):
        return f"PO: {self.PO_NO}\nPO DATE: {self.PO_DATE}\nInvoice Date: {self.INVOICE_DATE}\nCompany Name: {self.COMPANY_NAME}\n Billed Amount(without TaX):{self.TOTAL_WITHOUT_TAX}\n Billed Amount (with Tax): {self.TOTAL_WITH_TAX}"

