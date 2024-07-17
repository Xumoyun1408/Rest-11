from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import All_Xarajat
from .serializers import All_XarajatSerializer

class All_XarajatView(ListAPIView):
    serializer_class = All_XarajatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return All_Xarajat.objects.filter(user=user)
