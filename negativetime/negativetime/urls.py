from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from docit.views import ProjectListCreateView, SectionListView, UserRetrieveView, home


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'negativetime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^projects/$', ProjectListCreateView.as_view(), name='projects'),
    url(r'^projects/(?P<pk>\d+)/$', SectionListView.as_view(), name='sections'),
    url(r'^user/$', UserRetrieveView.as_view(), name='user'),

    url(r'^$', home, name='user'),
)
