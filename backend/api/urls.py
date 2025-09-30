from django.contrib import admin
from django.urls import path
from . import views
print("api. url---------")
urlpatterns=[
    path('',views.Studentcl.as_view(),name='student'),
    path('student/',views.Studentcl.as_view(),name='student'),
    path('student/<int:pk>',views.StudentRUD.as_view(),name='student'),
    path("hello/", views.hello, name="hello"),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]