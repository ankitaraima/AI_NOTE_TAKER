from django.contrib import admin
from django.urls import path, include
from noteTakerApp.views import NoteTaker
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('noteTakerApp.urls')),  # Keeps API routes
    # path('signup/', NoteTaker.signup),  # ✅ Make sure the signup route is included!
    # path('signUpProcess/', NoteTaker.signUpProcess, name='signUpProcess'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
