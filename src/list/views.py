from django.views.generic import View
from django.http import HttpResponse
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
#from blog.forms import handle_uploaded_file

from djangofirsttouch.utils import render_to

from list.forms import PriceForm


class PriceShow(View):

    @render_to("list/list.jinja")
    def get(self, request):
        form = PriceForm()
        return {'form': form}

    # @render_to("blog/blog.jinja")
    # def post(self,request):
    #     user = request.user
    #     form = BlogForm(request.POST.copy())
    #
    #     if user.is_authenticated():
    #         if form.is_valid():
    #             field = form.cleaned_data['text']
    #             form.save()
    #         return {'form': form}
    #     else:
    #         return {'redirect': '/account/login.jinja'}

    # def current_datetime(request):
    #     date = datetime.datetime.now()
    #     return date
    # Imaginary function to handle an uploaded file.

    @render_to("list/list.jinja")
    def post(self, request):
        if request.method == 'POST':
            form = PriceForm(request.POST, request.FILES)
            if form.is_valid():
                form.handle_uploaded_file(request.FILES['attachment'])
                form.save()
            return {'redirect': "/list/"}
        else:
            form = PriceForm()
            return {'form': form}