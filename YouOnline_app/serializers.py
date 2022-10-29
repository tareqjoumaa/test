from rest_framework import serializers
from YouOnline_app.models import youonline


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = youonline
        fields = '__all__'



