from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Noticia
from .serializers import NoticiaSerializer

@api_view(['GET'])
def listar_noticias(request):

    noticias = Noticia.objects.all()

    serializer = NoticiaSerializer(noticias, many=True)

    return Response(serializer.data)

from django.db.models import Count

@api_view(['GET'])
def estatisticas(request):

    total = Noticia.objects.count()

    fontes = Noticia.objects.values("fonte").annotate(total=Count("fonte"))

    ultima = Noticia.objects.order_by("-data").first()

    return Response({
        "total_noticias": total,
        "fontes": list(fontes),
        "ultima_noticia": ultima.titulo if ultima else None
    })

import csv
from django.http import HttpResponse
from .models import Noticia

def exportar_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="noticias.csv"'

    writer = csv.writer(response)

    writer.writerow(['ID', 'Titulo', 'Link', 'Fonte', 'Data'])

    noticias = Noticia.objects.all()

    for noticia in noticias:
        writer.writerow([
            noticia.id,
            noticia.titulo,
            noticia.link,
            noticia.fonte,
            noticia.data
        ])

    return response
