from django.shortcuts import render
from links.models import Link
from django.views.generic import ListView
from allauth.account.decorators import verified_email_required


class Dashboard(ListView):
    model = Link
    template_name = "authapp/dashboard.html"
    paginate_by = 10

    def get_queryset(self):
        self.request.session['saved_back_url'] = self.request.get_full_path()
        return self.request.user.link_like.all()

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['welcome'] = "Welcome to your space on How Should I Learn That"
        return context


def privacy(request):
    return render(request, 'authapp/privacy.html', {})
