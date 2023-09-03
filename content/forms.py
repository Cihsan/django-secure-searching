from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'
        # fields = ['name', 'brand', 'category','description','features','price','colors','sizes', 'availability', 'rating','num_reviews','seller_name','seller_rating']