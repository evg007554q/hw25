from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from apptraining.apps import ApptrainingConfig


app_name = ApptrainingConfig.name

urlpatterns = [
    # path('', cache_page(60)(index), name='index'),
    path('admin/', admin.site.urls),
    # path('products/', productListView.as_view(), name='products'),
    # path('<int:pk>/product/', cart_product, name='cart_product'),
    # path('product/create/', ProductCreateView.as_view(), name='product_create'),
    # path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    # path('info/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
]
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
