from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Inspection
from .serializers import SignupSerializer, InspectionSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger('api')  

class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer

class InspectionCreateView(generics.CreateAPIView):
    serializer_class = InspectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            logger.info(f"POST /inspection by {self.request.user}")
            serializer.save(inspected_by=self.request.user)
        except Exception as e:
            logger.error(f"Error during inspection creation by {self.request.user}: {str(e)}", exc_info=True)
            raise

class InspectionDetailView(generics.RetrieveAPIView):
    serializer_class = InspectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            return Inspection.objects.filter(inspected_by=self.request.user)
        except Exception as e:
            logger.error(f"Error fetching inspection details for {self.request.user}: {str(e)}", exc_info=True)
            return Inspection.objects.none()

class InspectionUpdateStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            inspection = get_object_or_404(Inspection, pk=pk, inspected_by=request.user)
            status_value = request.data.get('status')

            if not status_value:
                logger.warning(f"Missing status value in PATCH /inspection/{pk} by {request.user}")
                return Response({'error': 'Status is required'}, status=400)

            if status_value not in ['reviewed', 'completed']:
                logger.warning(f"Invalid status '{status_value}' in PATCH /inspection/{pk} by {request.user}")
                return Response({'error': 'Invalid status'}, status=400)

            inspection.status = status_value
            inspection.save()
            logger.info(f"PATCH /inspection/{pk} by {request.user} updated to '{status_value}'")
            return Response({'status': 'updated'})

        except Exception as e:
            logger.error(f"Error in PATCH /inspection/{pk} by {request.user}: {str(e)}", exc_info=True)
            return Response({'error': 'Server error'}, status=500)

class InspectionListView(generics.ListAPIView):
    serializer_class = InspectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            status_filter = self.request.query_params.get('status')
            qs = Inspection.objects.filter(inspected_by=self.request.user)
            if status_filter:
                logger.info(f"GET /inspection-list/?status={status_filter} by {self.request.user}")
                qs = qs.filter(status=status_filter)
            else:
                logger.info(f"GET /inspection-list/ by {self.request.user}")
            return qs
        except Exception as e:
            logger.error(f"Error in GET /inspection-list/ by {self.request.user}: {str(e)}", exc_info=True)
            return Inspection.objects.none()

