from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author', 'genre']

# Create your views here.
