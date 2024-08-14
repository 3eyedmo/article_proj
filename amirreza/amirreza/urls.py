from django.contrib import admin
from django.urls import path, include
from .views import amirreza_handler


urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/<int:pk>/', amirreza_handler),
    path('articles/', include('articles.urls', namespace='articles'))
]


# Dajngo Architecture/Pattern:   MTV
# 1: Template
# 2: View
# 3: Model