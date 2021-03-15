from django.shortcuts import get_object_or_404, render
from .models import Link, Tag
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from .forms import SearchForm, LinkForm
from django.views.generic import ListView


class SearchList(ListView):
    model = Link
    template_name = "links/index.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        self.request.session['saved_back_url'] = self.request.get_full_path()
        if form.is_valid():
            return queryset.search(**form.cleaned_data)

        else:
            return queryset.filter(approved=True).order_by('-created_at')[:5]

    def get_context_data(self, **kwargs):
        searched = False
        list_title = "Recently posted links"
        form = SearchForm(self.request.GET)
        if form.is_valid():
            searched = True
            list_title = "Search results"
        context = super(SearchList, self).get_context_data(**kwargs)
        context['list_title'] = list_title
        context['searched'] = searched
        context['all_tags'] = [tag.name for tag in Tag.objects.all()]
        context['form'] = form
        return context


class LinkDetailView(DetailView):

    model = Link

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Link, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        saved_back_url = self.request.session.get("saved_back_url")
        if saved_back_url:
            data["saved_back_url"] = saved_back_url
        else:
            data["saved_back_url"] = reverse('links:index')
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


def like(request, pk):
    link = get_object_or_404(Link, id=request.POST.get('like_id'))
    if link.likes.filter(id=request.user.id).exists():
        link.likes.remove(request.user)
    else:
        link.likes.add(request.user)

    return HttpResponseRedirect(reverse('links:detail', args=[str(pk)]))


def suggest(request):
    if request.method == 'POST':
        form = LinkForm(request.POST or None)
        if form.is_valid():
            new_link = form.save(commit=False)
            new_link.approved = False
            new_link.save()
            return HttpResponseRedirect(reverse('links:index'))
    else:
        form = LinkForm()

    context = {
        "form": form
    }

    saved_back_url = request.session.get("saved_back_url")
    if saved_back_url:
        context["saved_back_url"] = saved_back_url
    else:
        context["saved_back_url"] = reverse('links:index')

    return render(request, 'links/suggest.html', context=context)