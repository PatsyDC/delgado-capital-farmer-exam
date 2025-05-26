from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('form/', views.Index, name='index'),
    path('cotizacion/', views.CotizacionAPIView.as_view(), name='cotizacion'),  # ✅ Agregado
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
