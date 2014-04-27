from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from docit.views import ProjectListCreateView, LoginView, LogoutView, SectionListView, UserRetrieveView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'negativetime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),


    url(r'^projects/$', ProjectListCreateView.as_view(), name='projects'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^projects/(?P<project_id>\d+)/$', SectionListView.as_view(), name='sections'),
    url(r'^user/$', UserRetrieveView.as_view(), name='user'),
)
