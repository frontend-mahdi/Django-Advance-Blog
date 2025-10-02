from rest_framework import serializers
from ...models import Post,Category

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):
    #1 content = serializers.ReadOnlyField()
    #2 content = serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url =serializers.SerializerMethodField(method_name='get_abs_url')
    class Meta:
        model = Post
        fields = '__all__'
        fields = ['id','title','content','status','snippet','relative_url','absolute_url','created_date','published_date']
        #3 read_only_fields = ['content']
    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
