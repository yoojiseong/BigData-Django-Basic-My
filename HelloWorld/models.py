#변경 해야함
from pip._internal import models


class DjangoModel(models.Model):
    name = models.CharField(max_length=100)