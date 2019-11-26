from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Post
        fields = ('id', 'title', 'content', 'date_created', 'author')
        extra_kwargs = {
            'author': {
                'read_only': True
            }
        }