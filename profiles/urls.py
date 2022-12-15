from django.urls import path
from rest_framework import routers

from profiles.views import CustomerUserProfileViewSet
from profiles.views.customers_users_profiles_viewset import CustomersUsersProfilesViewSet, PreguntasViewSet, \
    PreguntasReto2ViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('user', CustomerUserProfileViewSet.as_view(), name="customer_user_profile_get_or_create_or_update"),
    path('user/<int:pk>', CustomerUserProfileViewSet.as_view(), name="customer_user_profile_get_one"),

    path('users', CustomersUsersProfilesViewSet.as_view()),
    path('listaPreguntas', PreguntasViewSet.as_view()),
    path('listaPreguntasReto2', PreguntasReto2ViewSet.as_view()),
]
