from django.urls import path

from adminapp.views import index, admin_users_read, admin_users_create, admin_users_update, admin_users_delete, \
    admin_products_read, admin_products_create, admin_products_delete, admin_products_update

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', admin_users_read, name='admin_users_read'),
    path('admin-users-create/', admin_users_create, name='admin_users_create'),
    path('admin-users-update/<int:id>/', admin_users_update, name='admin_users_update'),
    path('admin-users-delete/<int:id>/', admin_users_delete, name='admin_users_delete'),
    path('admin-products-read/', admin_products_read, name='admin_products_read'),
    path('admin-products-create/', admin_products_create, name='admin_products_create'),
    path('admin-products-update/<int:id>/', admin_products_update, name='admin_products_update'),
    path('admin-products-delete/<int:id>/', admin_products_delete, name='admin_products_delete'),
]
