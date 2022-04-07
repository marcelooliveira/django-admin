from django.http import HttpResponse

from django.template import loader
from custom.models import Category

def index(request):
  categories = Category.objects.order_by('id')
  template = loader.get_template('report.html')
  context = {
      'Categories': categories
  }
  return HttpResponse(template.render(context, request))
