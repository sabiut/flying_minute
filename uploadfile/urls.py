from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('model_form_upload/', views.model_form_upload, name='upload_page'),
    path('displayfile/', views.displayfile, name='displayfile'),
    path('view_file/', views.view_file, name ='view_file'),
    path(r'<int:paper_id>/delete_paper/', views.drop_paper, name='drop_paper'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
