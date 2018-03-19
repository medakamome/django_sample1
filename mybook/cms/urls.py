from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
            # ����
            path('book/', views.book_list, name='book_list'),   # �ꗗ
            path('book/add/', views.book_edit, name='book_add'),  # �o�^
            path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),  # �C��
            path('book/del/<int:book_id>/', views.book_del, name='book_del'),   # �폜
            ]
