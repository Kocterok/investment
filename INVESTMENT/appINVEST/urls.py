from django.urls import path
from . import views




urlpatterns = [
    path('', views.index),
    path('about', views.abaut),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('add_asset/', views.add_asset, name='add_asset'),
    path('delete_asset/', views.delete_asset, name='delete_asset'),
    
]

# urlpatterns = [
#     path('portfolio/', portfolio_view, name='portfolio_view'),
#     path('add_asset/', add_asset, name='add_asset'),
#     path('remove_asset/<int:asset_id>/', remove_asset, name='remove_asset'),
# ]