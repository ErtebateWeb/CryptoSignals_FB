from django.urls import path
from .views import home
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
      path('', home),
#     path('submit_signals', submit_signals),
#    # path('products/<pk>', ProductDetailView.as_view()),
#     path('signal_details/<id>', binary_detail_view),

]
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)