from rest_framework import viewsets, permissions
from .models import UserProfile, Category, CarMake, Model, Car, Bet, Comment
from .serializers import *
from allauth.account.views import SignupView
from .forms import CustomSignupForm
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class CustomSignupView(SignupView):
    form_class = CustomSignupForm


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        user_profile = self.get_object()
        if user_profile.user == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("Вы не можете изменить профиль другого пользователя")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CarMakeViewSet(viewsets.ModelViewSet):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'car_make', 'model', 'price']
    search_fields = ['car_name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.user == self.request.user:
            serializer.save()
        else:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Вы не можете изменить машину другого пользователя")


class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
