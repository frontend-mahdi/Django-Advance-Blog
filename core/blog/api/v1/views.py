from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from ...models import Post


@api_view()
def api_post_list_view(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view()
def api_post_detail_view(request, id):
    post = get_object_or_404(Post, pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)
