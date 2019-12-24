from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin
from .models import books1
from .ser import creSerializer


# 查看
class Detail(GenericViewSet, ListModelMixin):
    queryset = books1.objects.all()
    serializer_class = creSerializer


# 增加
class CreateCollege(GenericViewSet, CreateModelMixin):
    queryset = books1.objects.all()
    serializer_class = creSerializer


# 删除
class DelCollege(GenericViewSet, DestroyModelMixin):
    queryset = books1.objects.all()
    serializer_class = creSerializer


# 修改
class UpdateCollege(GenericViewSet, UpdateModelMixin):
    queryset = books1.objects.all()
    serializer_class = creSerializer
