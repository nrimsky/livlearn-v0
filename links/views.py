from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from .models import Link
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.db.models import Q
from .forms import SearchForm


# def index(request):
#     latest_links = Link.objects.order_by('-created_at')[:5]
#     template = loader.get_template('links/index.html')
#     return HttpResponse(template.render({'object_list': latest_links, "list_title": "Recent links posted"}, request))
#



def search_view(request):
    form = SearchForm(request.GET)
    list_title = "Recently posted links"
    searched = False
    if form.is_valid():
        list_title = "Search results"
        links = Link.objects.search(**form.cleaned_data)
        searched = True
    else:
        links = Link.objects.filter(approved=True).order_by('-created_at')[:5]
    return render(request, "links/index.html", {"form": form, "object_list": links, "list_title": list_title, "searched": searched})


# class SearchResultsView(ListView):
#     model = Link
#     template_name = 'links/index.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         object_list = Link.objects.filter(
#             Q(name__icontains=query) | Q(description__icontains=query)
#         )
#         return object_list
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["list_title"] = "Search results"
#         return context

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