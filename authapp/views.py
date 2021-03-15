from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm
from links.models import Link
from django.views.generic import ListView


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


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'authapp/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'authapp/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'authapp/edit.html', context=context)