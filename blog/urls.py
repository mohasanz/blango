# other imports
from .views import index
from django.urls import path

urlpatterns = [
    # other patterns
    path("", index)
]