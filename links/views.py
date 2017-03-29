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


class NewSubmissionView(CreateView):
    model = Link
    fields = (
        'title', 'url',
    )

    template_name = 'new_submission.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NewSubmissionView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        new_link = form.save(commit=False)
        new_link.submitted_by = self.request.user
        new_link.save()

        self.object = new_link
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('home')


class HomeView(TemplateView):
    template_name = 'home.html'
