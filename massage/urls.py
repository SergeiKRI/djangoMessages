from django.urls import path
from django.views.decorators.cache import cache_page

from massage.apps import MassageConfig


app_name = MassageConfig.name

urlpatterns = [
    # path('', ProductsListView.as_view(), name='products_list'),
    # path('contacts/', contact, name='contacts'),
    # path('product/<int:pk>/', cache_page(60)(ProductsDetailView.as_view()), name='products_detail'),
    # path('product/create/', ProductsCreateView.as_view(), name='product_create'),
    # path('product/<int:pk>/update/', ProductsUpdateView.as_view(), name='product_update'),
    # path('product/<int:pk>/delete/', ProductsDeleteView.as_view(), name='product_delete'),
    #
    # path('record/', BlogRecordListView.as_view(), name='record_list'),
    # path('record/create/', BlogRecordCreateView.as_view(), name='record_create'),
    # path('record/<int:pk>/', BlogRecordDetailView.as_view(), name='record_detail'),
    # path('record/<int:pk>/update/', BlogRecordUpdateView.as_view(), name='record_update'),
    # path('record/<int:pk>/delete/', BlogRecordDeleteView.as_view(), name='record_delete'),
]
