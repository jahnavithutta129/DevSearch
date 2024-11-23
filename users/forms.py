from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Skill,Message

class CustomUserCreationForm(UserCreationForm): #now we have al the attributes as that of usercreationform
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2'] #one is the actual password and the other is the confirmation password
        labels={
            'first_name':'Name',
        } 

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm , self).__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            #the input field is added to the actual model form to make it styled and customized

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['name','email','username','location','bio','short_intro','profile_image',
        'social_github','social_linkedin','social_twitter','social_youtube','social_website']
    def __init__(self,*args,**kwargs):
        super(ProfileForm , self).__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            #the input field is added to the actual model form to make it styled and customized

class SkillForm(ModelForm):
    class Meta:
        model=Skill
        fields='__all__'
        exclude=['owner']
    def __init__(self,*args,**kwargs):
        super(SkillForm , self).__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            #the input field is added to the actual model form to make it styled and customized 

class MessageForm(ModelForm):
    class Meta:
        model=Message
        fields=['name','email','subject','body']
    def __init__(self,*args,**kwargs):
        super(MessageForm , self).__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            #the input field is added to the actual model form to make it styled and customized