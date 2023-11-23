from __future__ import annotations

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from core_viewsets.custom_viewsets import CreateViewSet
from core_viewsets.custom_viewsets import ListViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import (
    RefreshToken,
    AccessToken,
    OutstandingToken,
    BlacklistedToken,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render
from .models import CountryPopulation
from .forms import AdvancedSearchForm
from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework.views import APIView


# Create your views here.


class RegisterViewSet(CreateViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = RegisterSerializer
    queryset = get_user_model().objects.all()

    def create(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password", None)
        phone_number = request.data.get("phone_number")

        # TODO: Validations
        if not email or not password or not phone_number:
            return Response(
                {"code": 400, "message": "Incomplete data"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = get_user_model().objects.create_user(request.data)

        return Response(
            {"code": 200, "message": "success", "user_id": user._get_pk_val()},
        )


# class LoginViewSet(CreateViewSet):
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = LoginSerializer

#     def create(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         # TODO: validation
#         user_obj = get_user_model().objects.get(email=email, password=password)
#         # TODO:  generate token with jwt library
#         # TODO: Update the Login activity


#         user_obj.last_login = timezone.now()
#         return Response(
#             {
#                 'code': 200,
#                 'message': 'success',
#                 'access_token': '',
#                 'refresh_token': 'refresh_token',
#                 'user_id': user_obj.pk,
#                 'name': user_obj.first_name,
#                 'email': user_obj.email,
#                 'last_login': user_obj.last_login,
#             },
#         )


class LoginViewSet(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        # TODO: validation

        try:
            user_obj = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            return Response(
                {"code": 400, "message": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # TODO:  generate token with jwt library
        # TODO: Update the Login activity
        if not user_obj.check_password(password):
            return Response(
                {"code": 400, "message": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Generate tokens
        refresh = RefreshToken.for_user(user_obj)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        user_obj.last_login = timezone.now()
        user_obj.save()

        return Response(
            {
                "code": 200,
                "message": "success",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user_id": user_obj.pk,
                "name": user_obj.first_name,
                "email": user_obj.email,
                "last_login": user_obj.last_login,
            },
            status=status.HTTP_200_OK,
        )


class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]  # ToDO Specify Auth class
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            RefreshToken(refresh_token).blacklist()
            return Response(
                {"message": "Logout successful."}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST
            )


class MeViewSet(ListViewSet):
    authentication_classes = [JWTAuthentication]  # ToDO Specify Auth class
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer  # ToDO Specify serializer_class class
    queryset = get_user_model().objects.all()

    def list(self, request, *args, **kwargs):
        # ToDO:  Add your code
        user = request.user
        serializer = self.serializer_class(user)

        return Response(serializer.data)


def home(request):
    form = AdvancedSearchForm(request.GET)
    data = CountryPopulation.objects.all()

    if form.is_valid():
        country = form.cleaned_data.get("country")
        min_pop1980 = form.cleaned_data.get("min_pop1980")
        max_pop1980 = form.cleaned_data.get("max_pop1980")

        # Filter data based on form input
        if country:
            data = data.filter(country__icontains=country)
        if min_pop1980:
            data = data.filter(pop1980__gte=min_pop1980)
        if max_pop1980:
            data = data.filter(pop1980__lte=max_pop1980)

        # Add more filters for other fields as needed

    return render(request, "home.html", {"data": data, "form": form})
