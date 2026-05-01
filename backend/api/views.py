from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Negocio, Evento
from .serializers import NegocioSerializer, EventoSerializer
import requests
import urllib.parse

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class NewsAPIView(APIView):
    def get(self, request):
        api_key = 'e9707b96692d4e51b5340afdb151c8c4'
        
        # Haciendo la petición directamente desde el servidor Django
        # Bypasses browser CORS restrictions completely
        url = f"https://newsapi.org/v2/everything?q=colombia&language=es&apiKey={api_key}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'ok' and len(data.get('articles', [])) > 0:
                    articles = []
                    for article in data['articles']:
                        # Filter out [Removed] articles that NewsAPI sometimes returns
                        if article.get('title') == '[Removed]' or article.get('title') is None:
                            continue
                            
                        articles.append({
                            'title': article.get('title'),
                            'date': article.get('publishedAt'),
                            'summary': article.get('description') or 'Haga clic para leer más sobre esta noticia.',
                            'image': article.get('urlToImage') or 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?q=80&w=600&auto=format&fit=crop',
                            'link': article.get('url')
                        })
                    
                    # Take only up to 6 articles
                    articles = articles[:6]
                    
                    if len(articles) > 0:
                        return Response({'status': 'ok', 'articles': articles})
            else:
                print(f"NewsAPI returned status code: {response.status_code}")
                print(f"Response: {response.text}")
            
            # Fallback if NewsAPI fails
            return self.get_fallback()
        except Exception as e:
            print("Error fetching news:", str(e))
            return self.get_fallback()
            
    def get_fallback(self):
        fallback_news = [
            {
                'title': 'Avanzan proyectos de infraestructura en Colombia',
                'date': '2024-10-28T00:00:00Z',
                'summary': 'El gobierno nacional anunció nuevos planes para la mejora de la red vial en diversas regiones del país.',
                'image': 'https://images.unsplash.com/photo-1541888086925-920a0f4439c4?q=80&w=600&auto=format&fit=crop',
                'link': 'https://www.google.com/search?q=obras+viales+Colombia&tbm=nws'
            },
            {
                'title': 'Turismo en Colombia alcanza cifras récord',
                'date': '2024-10-25T00:00:00Z',
                'summary': 'Las principales ciudades y destinos turísticos del país reportan un aumento significativo en la llegada de visitantes internacionales.',
                'image': 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=600&auto=format&fit=crop',
                'link': 'https://www.google.com/search?q=Turismo+Colombia&tbm=nws'
            },
            {
                'title': 'Nuevos impulsos a la agricultura nacional',
                'date': '2024-10-20T00:00:00Z',
                'summary': 'Miles de familias campesinas en toda Colombia están recibiendo apoyo tecnológico para mejorar sus cultivos.',
                'image': 'https://images.unsplash.com/photo-1595841696650-6e3e5de3a07b?q=80&w=600&auto=format&fit=crop',
                'link': 'https://www.google.com/search?q=Agricultura+Colombia&tbm=nws'
            }
        ]
        return Response({'status': 'fallback', 'articles': fallback_news})
