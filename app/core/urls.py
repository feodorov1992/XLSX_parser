from django.urls import path

from core.views import FileUploadView, UploadHistoryListView, UploadedFileDetailView

urlpatterns = [
    path('', FileUploadView.as_view(), name='home'),
    path('files', UploadHistoryListView.as_view(), name='history'),
    path('files/<uuid:pk>/detail', UploadedFileDetailView.as_view(), name='detail')
]
