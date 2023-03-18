from rest_framework import generics, mixins, viewsets

from .models import User
from .serializers import UserSerializer, UserSerializerWithFullName


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.version == "0.2":
            return UserSerializerWithFullName
        return UserSerializer
