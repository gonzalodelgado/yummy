import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse_lazy
from biblion.models import Post


def can_delete_post(user):
    return user.is_staff


class AjaxDeleteView(DeleteView):
    def delete(self, request, *args, **kwargs):
        """
        Deletes fetched object from database and responds with JSON
        to AJAX requests, and with a redirect to the success url to
        normal ones.
        """
        if not can_delete_post(request.user):
            return HttpResponseBadRequest()
        default_response = super(AjaxDeleteView,
                                 self).delete(request, *args, **kwargs)
        if request.is_ajax():  # Respond with JSON to AJAX requests
            return HttpResponse(json.dumps({'deleted': True}),
                                content_type='application/json')
        # otherwise just behave like a normal DeleteView
        return default_response


class DeletePostView(AjaxDeleteView):
    model = Post
    success_url = reverse_lazy('blog')
    pk_url_kwarg = 'post_pk'

terminate_post = DeletePostView.as_view()
