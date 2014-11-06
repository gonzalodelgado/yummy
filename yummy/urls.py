from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = patterns(
    "",
    url(r"^admin/", include(admin.site.urls)),
    url(r"^terminate/(?P<post_pk>\d+)/$",
        'post_terminator.views.terminate_post', name='terminate-post'),
    url(r"^unterminate/(?P<post_pk>\d+)/$",
        'post_terminator.views.unterminate_post', name='unterminate-post'),
    url(r"", include("biblion.urls")),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
