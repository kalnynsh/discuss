from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import View
from django.utils import timezone

from links.models import Link
from links.forms import CommentModelForm
from links.models import Comment


class HomeView(TemplateView):
    template_name = 'home.html'
