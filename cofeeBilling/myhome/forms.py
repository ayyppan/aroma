from django import forms
from django.core import validators
from django.contrib.auth.models import User
from myhome.models import Service_type, UserProfileInfo

def check_for_0(value):
    if value == 0:
        raise forms.ValidationError("Quantity should not be 0!!")


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class FormCustomer(forms.Form):
    Company_Name = forms.CharField()
    Company_addr1 = forms.CharField()
    Company_addr2 = forms.CharField()
    Company_addr3 = forms.CharField()
    Company_addr4 = forms.CharField()




class FormName(forms.Form):
    # Company_Name = forms.CharField()
    # Company_addr1 = forms.CharField()
    # Company_addr2 = forms.CharField()
    # Company_addr3 = forms.CharField()
    # Company_addr4 = forms.CharField()
    Service_name = forms.CharField()
    Quantity = forms.IntegerField(validators=[check_for_0])
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        Serv_NM = all_clean_data['Service_name']

        avServ=["Coffee Powder","Sugar","Tea powder","Sugar cubs","Suger sachsets","Stirrers","Paper Cups","Rental Charges","Manual Coffee filter",
                "Minimum Guarantee (MG)","Milk Boiler 5 Litres","Green Tea","Lemon Tea","Horlicks Sachets 10G","Boost Sachetes 10G","Badam Powder Mix",
                "Milk","Tetley Tea bag (Normal)","Filter coffee","Brew Tea","Hot Milk","Wood Stirrer"]
        
        if Serv_NM not in avServ:
            raise forms.ValidationError(f"There is no service for {Serv_NM}")

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']

        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT")
            return botcatcher