from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['name', 'brand', 'category', 'description', 'features', 'price', 'colors', 'sizes', 'availability', 'rating', 'num_reviews', 'seller_name', 'seller_rating','img']
    def __init__(self, *args, **kwargs):
        super(ContentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'brand': forms.TextInput(attrs={'class': 'form-control'}),
        #     'category': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'features': forms.TextInput(attrs={'class': 'form-control'}),
        #     'price': forms.IntegerField(attrs={'class': 'form-control'}),
        #     'colors': forms.TextInput(attrs={'class': 'form-control'}),
        #     'sizes': forms.TextInput(attrs={'class': 'form-control'}),
        #     'availability': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Use CheckboxInput for boolean field
        #     'rating': forms.Select(attrs={'class': 'form-control'}),
        #     'num_reviews': forms.IntegerField(attrs={'class': 'form-control'}),
        #     'seller_rating': forms.Select(attrs={'class': 'form-control'})
        # }