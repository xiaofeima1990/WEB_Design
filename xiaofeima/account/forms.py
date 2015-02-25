from django import forms
from account.models import UserProfile
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    
    
    #must be
    first_name = forms.CharField(help_text="Please enter your first name")
    last_name  = forms.CharField(help_text="Please enter your last name")
    birth_date = forms.DateField(help_text="Please enter your birth date", required=False)
    University = forms.CharField(help_text="Please enter your university")



    #suggest
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)
    motto   = forms.CharField(help_text="Please enter your motto")

    #optional
    website = forms.URLField(help_text="Please enter your website.", required=False)
    province = forms.CharField(required=False)
    city = forms.CharField(required=False)





    class Meta:
        model = UserProfile
        fields = ['first_name','last_name', 'University','birth_date','province','city','picture']