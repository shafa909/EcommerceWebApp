
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin
from .views import Shafa,home_page ,about ,contact ,login_page ,register_page
from products.views import (ProductListView,
                        product_list_view,
                        ProductDetailView,
                        product_detail_view,
                        ProductFeaturedDetailView,
                        ProductFeaturedListView,
                        ProductSlugDetailView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page),
    url(r'^about/$', about),
    url(r'^contact/$', contact),
    url(r'^login/$', login_page),
    url(r'^register/$', register_page),
    url(r'^product/$', ProductListView.as_view()),
    url(r'^product-f/$', product_list_view),
    #url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view()), #detail view
    url(r'^product-f/(?P<pk>\d+)/$', product_detail_view), #detail view
    url(r'^featured/$', ProductFeaturedListView.as_view()),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^product/(?P<slug>[\w-]+)/$', ProductSlugDetailView.as_view())

 


]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)