from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteTaker
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
router.register(r'noteTaker', NoteTaker, basename='noteTaker')

urlpatterns = [
    path('', include(router.urls)),  # Keeps API endpoints
    path('signup/', NoteTaker.signup, name='signup'),
    path('signin/', NoteTaker.signin, name='signin'),
    path('forget_password/', NoteTaker.forget_password, name='forget_password'),
    path('home/', NoteTaker.home, name='home'),  # ✅ Manually register signup URL
    path('change_password/', NoteTaker.change_password, name='change_password'),
    path('noteTaker/', NoteTaker.noteTaker, name='noteTaker'),
    path('profile/', NoteTaker.profile, name='profile'),
    path('history/', NoteTaker.history, name='history'), 
    path('logout/', NoteTaker.logout, name='logout'),       # ✅ Manually register signup URL

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


