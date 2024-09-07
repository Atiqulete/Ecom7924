from website.models import Category

def g_categories(request):
    g_cate = Category.objects.all()
    return {'g_cate': g_cate}