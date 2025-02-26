from attr import fields
from django import forms
from django.core import validators
from basic.models import relative, senior_citizen,CareTakerInfo
from django.contrib.auth.models import User

GENDER = [("Male","Male"),("Female","Female"),("Other","Other")]
ED = [('Matriculate','Matriculate'),('Intermediat',"Intermediat"),('Graduate',"Graduate")]
EXP = [('0-2 Years',"0-2 Years"),("2-4 years","2-4 years"),("4-6 Years","4-6 Years")]

class Form_senior(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item'}))
    number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control item'}))
    gender = forms.ChoiceField(choices=GENDER)
    address1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item'}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item'}))
    pin_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    profile_pic = forms.ImageField(allow_empty_file=True,widget=forms.FileInput(attrs={'class':'form-control item'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control item'}))


    class Meta:
        model = User
        fields = ("password")
        model = senior_citizen
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Form_senior, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False



class form_CareTakerInfo(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    number = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control item '}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    gender = forms.ChoiceField(choices=GENDER)
    adhar_num = forms.CharField(
        label="Adhaar Number",
        widget=forms.TextInput(attrs={'class':'form-control item '})
    )
    bank_num = forms.CharField(label="Bank Account number",widget=forms.TextInput(attrs={'class':'form-control item '}))

    Ed_q = forms.ChoiceField(choices=ED, label="Educational qualifications")
    exp = forms.ChoiceField(choices=EXP, label="Experience (in years)")

    address1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    pin_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    
    resume_drive = forms.URLField()
    profile_pic = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control item '}))

    class Meta:
        model = User
        fields = ("password")
        model = CareTakerInfo
        fields = '__all__'



class form_relative(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control item '}))
    gender = forms.ChoiceField(choices=GENDER)
    address1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    pin_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item '}))
    profile_pic = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control item '}))
    
    class Meta:
        model = User
        fields = ("password")
        model = relative
        fields = '__all__'


class senior_login(forms.ModelForm):
    class Meta:
        model = senior_citizen
        fields = ("name","number","password")

class caretaker_login(forms.ModelForm):
    class Meta :
        model = CareTakerInfo
        fields = ("name","number","password")

class relative_login(forms.ModelForm):
    class Meta:
        model = relative
        fields = ("name","number","password")