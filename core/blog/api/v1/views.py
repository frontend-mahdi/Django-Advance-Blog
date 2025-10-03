from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import DefaultPagination

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
'''

class PostList(ListCreateAPIView):
    """getting  list of posts and creating new post"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(RetrieveUpdateDestroyAPIView):
    """get and update and delete single post"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter()
'''

class PostModelViewSet (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category', 'author','status']
    search_fields = ['=title']
    ordering_fields = ['published_date', 'created_date']
    pagination_class = DefaultPagination

    @action(methods=['get'],detail=False)
    def get_ok(self,request):
        return Response({'detail':'ok'})

class CategoryModelViewSet (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
