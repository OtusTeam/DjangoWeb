from django import forms
from .models import Category, Product

'''class CreateCategoryForm(forms.Form):
    title = forms.CharField(max_length=200, label='Название категории')
    description = forms.CharField(label='Описание категории', widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40}
        )
    )
    
    def save(self):
        Category.objects.create(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description']
        )
        return Category.objects.last()'''

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'description',
        ]
        widgets = {'description': forms.Textarea(
            attrs={
                'rows': 3,
                'cols': 40
            })
        }
        labels = {
            'title': 'Введите название категории',
        }

class CreateProductForm(forms.ModelForm):
    template_name = 'product_form.html'
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'categories',
        ]
        widgets = {'description': forms.Textarea()}

