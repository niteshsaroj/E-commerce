from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import viewsets

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
