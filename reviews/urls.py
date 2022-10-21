from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reviews'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:reviews_pk>/', views.detail, name='detail'),
    path('<int:reviews_pk>/update/', views.update, name='update'),
    path('<int:reviews_pk>/delete/', views.delete, name='delete'),
    path('<int:reviews_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:reviews_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)