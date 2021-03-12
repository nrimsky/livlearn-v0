from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from .models import Link
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.detail import DetailView


def index(request):
    latest_links = Link.objects.order_by('-created_at')[:5]
    template = loader.get_template('links/index.html')
    return HttpResponse(template.render({'links': latest_links}, request))


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