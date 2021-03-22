from django.shortcuts import render
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def dashboard(request):
    request.session['saved_back_url'] = request.get_full_path()
    liked = request.user.link_like.all()
    paginator = Paginator(liked, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        "page_obj": page_obj,
        "is_paginated": page_obj.has_next(),
        "form": user_form,
        "welcome": "Your personal space on How Should I Learn"
    }
    return render(request,"authapp/dashboard.html", context=context)


def privacy(request):
    return render(request, 'authapp/privacy.html', {})
