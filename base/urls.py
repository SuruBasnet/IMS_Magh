from django.urls import path
from .views import DepartmentView, ResourceView, ResourceDetailView

urlpatterns = [
    path('department/',DepartmentView.as_view({'get':'list','post':'create'})),
    path('department/<int:pk>/',DepartmentView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('resource/',ResourceView.as_view()),
    path('resource/<int:pk>/',ResourceDetailView.as_view()),
]