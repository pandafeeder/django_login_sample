from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


class SomePage(generic.TemplateView):
    template_name = "registration/some_page.html"

    def post(self, request, *args, **kwargs):
	data = self.request.POST
	user = AuthenticationForm(data=self.request.POST)
	if user.is_valid():
	    login(self.request, user.get_user())
	    return HttpResponse("Welcome "+str(self.request.user))
	return HttpResponse("FAILED LOGIN")
