from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


'''
ModelSerializer : 직렬화 클래스를 만드는 바로가기
- 자동으로 결정된 필드 집합
- create(), update() 메서드에 대한 간단한 기본 구현
'''
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        # 스니펫 모델 활용
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

'''
# json으로 serializing (=forms)
class SnippetSerializer(serializers.Serializer):
    # serialized/deserialized 되는 필드를 정의한다.
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # widget=swidget 장고 양식 클래스의 텍스트영역
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        # 유효한 데이터가 들어오면 새 스니펫을 만들고 반환
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 유효한 데이터가 들어오면 기존의 스니펫을 업데이트하고 반환
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
'''