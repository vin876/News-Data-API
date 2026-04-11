from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Noticia
from .serializers import NoticiaSerializer

@api_view(['GET'])
def listar_noticias(request):

    noticias = Noticia.objects.all()

    serializer = NoticiaSerializer(noticias, many=True)

    return Response(serializer.data)
