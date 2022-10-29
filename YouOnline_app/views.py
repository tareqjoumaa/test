
# Create your views here.
from rest_framework import viewsets
from YouOnline_app.models import youonline
from YouOnline_app.serializers import postSerializer


class posts(viewsets.ModelViewSet):
    queryset = youonline.objects.all()
    serializer_class = postSerializer

