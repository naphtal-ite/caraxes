from django import forms
from django.contrib.auth.models import User
from .models import Author,Book
from django.contrib.auth.forms import UserCreationForm
'''
class AuthorForm(forms.ModelForm):
      class Meta:
	        exclude=('user',)
	        model = Author
	        fields = ( 'email', 'phone','firstname' ,'lastname')
			'''
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
class  BookForm(forms.ModelForm):
    class Meta:
        model =  Book
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	phone = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	

	class Meta:
		model = User
		fields = ('username', 'email', 'phone','fullname' ,'password1', 'password2')
        
def __init__(self):
		super(UserRegisterForm, self)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	






			

	