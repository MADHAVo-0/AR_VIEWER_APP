# ar_app/urls.py
from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('upload_model'), name='home'),  # Redirect root to upload page
    path('upload/', views.upload_model, name='upload_model'),
    path('view_ar/', views.view_ar_models, name='view_ar_models'),
        path('delete-model/<int:model_id>/', views.delete_model, name='delete-model'),

]
