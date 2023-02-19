from django.forms import ModelForm
from category_management.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude  = [ 'created', 'updated']
        fields = "__all__"
        
    
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs["class"] = "form-select js-select2"
        self.fields['project'].widget.attrs["class"] = "form-select js-select2"