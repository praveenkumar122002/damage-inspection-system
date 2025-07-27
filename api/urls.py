from django.urls import path
from .views import SignupView, InspectionCreateView, InspectionDetailView, InspectionUpdateStatusView, InspectionListView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('inspection/', InspectionCreateView.as_view(), name='create-inspection'),
    path('inspection/<int:pk>/', InspectionDetailView.as_view(), name='detail-inspection'),
    path('inspection/<int:pk>/status/', InspectionUpdateStatusView.as_view(), name='update-status'),
    path('inspection-list/', InspectionListView.as_view(), name='list-inspection'),
]
