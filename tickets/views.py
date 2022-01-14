from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movie, Reservation, Post
from rest_framework.decorators import api_view
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer, PostSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins, viewsets

from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly

#1 without REST and no modelquery
def no_rest_no_model(request):

    guests=[
        {
            'id':1,
            'name':'ehab',
            'mobile':123456789,
            
        },
        {
            'id':2,
            'name':'mohamed',
            'mobile':123456789,

        }
    ]
    return JsonResponse (guests,safe=False)


#2 no rest and from model 
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests':list(data.values('name','mobile'))
    }
    return JsonResponse(response)



# List == GET
# Create == POST
# pk query == GET 
# Update == PUT
# Delete destroy == DELETE

#3 Function based view
#3.1 GET POST 

@api_view(['GET','POST'])
def FBV_List(request):

    #Get
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests,many=True)
        return Response(serializer.data) 
    #POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

#3.1 GET POST DELETE

@api_view(['GET','PUT','DELETE'])
def FBV_pk(request,pk):
    try:
        guests = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Get
    if request.method == 'GET':
       
        serializer = GuestSerializer(guests)
        return Response(serializer.data) 
    #PUT
    elif request.method == 'PUT':
        serializer = GuestSerializer(guests, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    if request.method == 'DELETE':
        
        guests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

    

#4 CBV Class Based View
class CBV_List(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests,many=True)
        return Response(serializer.data)
    def post(self, request):
        
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        

        return Response(serializer.data ,status=status.HTTP_400_BAD_REQUEST)

#5 GET PUT DELET CBV Class Based View --> PK

class CBV_pk(APIView):
    
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    #get 
    def get (self,request,pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    #PUT
    def put(self,request,pk):
        guests = self.get_object(pk)
        serializer = GuestSerializer(guests,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK) 
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        guests=self.get_object(pk)
        guests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#5 Mixins 
#5.1 mixins list
class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

#5.2 mixins get put delete 
class mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    def get(self, request, pk):
        return self.retrieve(request)
    def put(self, request, pk):
        return self.update(request)
    def delete(self, request, pk):
        return self.destroy(request)

# 6 Generics 
#6.1 get and post
class generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

#6.2 get put and delete 
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

#7 viewsets
class viewsets_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class viewsets_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backend = [filters.SearchFilter]
    search_fields = ['movie']

class viewsets_reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = Reservation

#8 Find movie
@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(
        hall = request.data['hall'],
        movie = request.data['movie'],
    )
    serializer = MovieSerializer(movies, many= True)
    return Response(serializer.data)

#9 create new reservation 
@api_view(['POST'])
def new_reservation(request):

    movie = Movie.objects.get(
        hall = request.data['hall'],
        movie = request.data['movie'],
    )
    guest = Guest()
    guest.name = request.data['name']
    guest.mobile = request.data['mobile']
    guest.save()

    reservation = Reservation()
    reservation.guest = guest
    reservation.movie = movie
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)


#10 post author editor
class Post_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
