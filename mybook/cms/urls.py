from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
            # ‘Ğ
            path('book/', views.book_list, name='book_list'),   # ˆê——
            path('book/add/', views.book_edit, name='book_add'),  # “o˜^
            path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),  # C³
            path('book/del/<int:book_id>/', views.book_del, name='book_del'),   # íœ
            ]
