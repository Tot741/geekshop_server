from django.urls import path

from adminapp.views import index, admin_users_read, admin_users_create, admin_users_update, admin_users_delete, admin_products_read

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', admin_users_read, name='admin_users_read'),
    path('admin-users-create/', admin_users_create, name='admin_users_create'),
    path('admin-users-update/<int:id>/', admin_users_update, name='admin_users_update'),
    path('admin-users-delete/<int:id>/', admin_users_delete, name='admin_users_delete'),
    path('admin-users-delete/<int:id>/', admin_users_delete, name='admin_users_delete'),
    path('admin-products-read/', admin_products_read, name='admin_products_read'),
    ]
