from django import forms

from shop_app.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "description",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"cols": 40, "rows": 5}),
        }
        labels = {
            "name": "Category name",
        }
        help_texts = {
            "name": "Used for product categories (m2m)",
        }
    # name = forms.CharField(label="Category name", max_length=100)
    # description = forms.CharField(widget=forms.Textarea)
