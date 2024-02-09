from .models import Catagory,Tag

def get_all_categories(request):
    categories = Catagory.objects.all().order_by('name')
    return {'all_categories': categories}

def get_all_tags(request):
    tags = Tag.objects.all().order_by('name')
    return {'all_tags': tags}

