from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status,mixins
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView

from .serializers import PostSerializer
from ...models import Post

"""
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postView(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        post.delete()
        return Response(
            {"details": f"post with id={id} was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )
"""
'''
class PostList(APIView):
    """getting  list of posts and creating new post"""
    permission_classes=[IsAuthenticated]
    serializer_class = PostSerializer
    
    def get(self,request):
        """get list of posts"""
        posts = Post.objects.all()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        "create a new post"
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''
'''
class PostList(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    """getting  list of posts and creating new post"""
    permission_classes=[IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get(self,request,*args,**kwargs):
        """get list of posts"""
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        "create a new post"
        return self.create(request,*args,**kwargs)
    
'''

class PostList(ListCreateAPIView):
    """getting  list of posts and creating new post"""
    permission_classes=[IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
class PostDetail(APIView):
    """get and update and delete single post"""
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self,request,id):
        """get single post"""
        post = get_object_or_404(Post, pk=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        """update single post"""
        post = get_object_or_404(Post, pk=id)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        """delete single post"""
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response(
            {"details": f"post with id={id} was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )