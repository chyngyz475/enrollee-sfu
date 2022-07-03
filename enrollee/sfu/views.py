from django.http import (
    HttpResponse,
    HttpRequest,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.shortcuts import render,redirect




def index (request: HttpRequest) -> HttpResponse:
  if request.method == 'POST':
    if form.is_valid():
      return HttpResponseRedirect('')
    else:
      form = ()
  context = { }
  return render(request=request,
                template_name='index.html'
                ,context=context)
  
