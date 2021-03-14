from django.shortcuts import get_object_or_404, render
from .models import Link, Tag
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from .forms import SearchForm, LinkForm


def search_view(request):
    form = SearchForm(request.GET)
    list_title = "Recently posted links"
    searched = False
    all_tags = [tag.name for tag in Tag.objects.all()]
    if form.is_valid():
        list_title = "Search results"
        links = Link.objects.search(**form.cleaned_data)
        searched = True
    else:
        links = Link.objects.filter(approved=True).order_by('-created_at')[:5]
    return render(request, "links/index.html", {"form": form, "object_list": links, "list_title": list_title, "searched": searched, "all_tags": all_tags})



class LinkDetailView(DetailView):

    model = Link

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Link, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
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

    return render(request, 'links/suggest.html', context=context)