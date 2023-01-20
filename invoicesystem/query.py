import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'invoicesystem.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.backends import ModelBackend

from deliveryorder.models import DeliveryOrderForm

def run():
    content_type = ContentType.objects.get_for_model(DeliveryOrderForm)
    post_permission = Permission.objects.filter(content_type=content_type)
    print([perm.codename for perm in post_permission])

    user = User.objects.get(username='manager')
    group = Group.objects.get(name='Manager')

    # print(group.permissions.all())

    # for perm in post_permission:
    #     print(user.has_perm(perm))

    #Manager permissions
    #Salesman permissions
    #Courier permissions
    #Finance office permissions



    # print(user.get_group_permissions())


if __name__ == '__main__':
    run()

