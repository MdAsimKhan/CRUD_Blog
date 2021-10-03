from django.forms import ModelForm
from .models import AddBlog

class AddBlogForm(ModelForm):
    class Meta:
        model = AddBlog
        fields = '__all__'
