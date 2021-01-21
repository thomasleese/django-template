from django.contrib import admin
from django.urls import path


admin.site.site_header = "Project"
admin.site.site_title = "Project Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
]
