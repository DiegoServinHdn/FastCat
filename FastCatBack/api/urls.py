from django import urls
from django.urls import path
from .views import WorkspaceView, main

urlpatterns = [
    path('', main),
    path('workspace', WorkspaceView.as_view())
]
