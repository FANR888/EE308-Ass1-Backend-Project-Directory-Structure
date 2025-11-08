# contacts/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    """
    提供 /contacts/ 的 list, create
    提供 /contacts/<id>/ 的 retrieve, update, destroy
    """
    queryset = Contact.objects.all().order_by('-id')
    serializer_class = ContactSerializer

@api_view(['GET'])
def search_contact(request):
    """
    搜索接口: /search_contact/?q=关键词
    通过姓名或电话进行模糊查询（不区分大小写）
    返回 JSON 列表
    """
    q = request.query_params.get('q', '').strip()
    if not q:
        # 若 q 为空，则返回全部或空列表；这里返回全部以便前端兼容 reset 情况
        contacts = Contact.objects.all().order_by('-id')
    else:
        contacts = Contact.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q)
        ).order_by('-id')

    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)
