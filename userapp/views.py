from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from .serializers import UserModelSerializer
from .models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
   