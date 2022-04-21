from django.urls.conf import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    re_path('^$',views.index,name='home'),
    path('library',views.library,name='library'),
    path('newbook',views.new_book,name='newbook'),
    path('my_book/<int:id>',views.book_details,name='my_book'),
    path('newreview/<int:id>',views.new_review,name='newreview'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)