from django.conf.urls import patterns, include, url
#from django.conf import settings
from booklib import settings
from booklib.settings import MEDIA_ROOT
from control_panel.orders.views import CustomersList
from control_panel.orders.views import CustomerDetails
from control_panel.library.views import BookList, AuthorList, BooksDetail, AuthorsDetail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'library.views.index'),
    url(r'^library/$', 'library.views.index'),
    url(r'^library/books/$', 'library.views.index'),
    url(r'^library/books/(\d+)/$', 'library.views.bookCard'),
    url(r'^library/authors/$', 'library.views.authors'),
    url(r'^library/authors/(\d+)/$', 'library.views.authorsCard'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT, }),
    url(r'^orders/$', CustomersList.as_view(), name='order_list.html'),
    url(r'^orders_list/(?P<pk>\d+)/$', CustomerDetails.as_view(), name='customer.html'),
    url(r'^registration/$', 'control_panel.registration.views.registrate'),
    url(r'^login/$', 'control_panel.registration.views.log_in'),
    url(r'^admin/', include(admin.site.urls)),
)
