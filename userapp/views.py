from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

from .models import CustomUser
from .serializers import UserCustomModelSerializer, UserModelSerializer


class UserModelViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer


class UserListAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    # serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == "v2":
            return UserCustomModelSerializer
        return UserModelSerializer
