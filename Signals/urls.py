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