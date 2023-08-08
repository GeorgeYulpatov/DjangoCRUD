# Импорт встроенных моделей Django.
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
# Импорт ObjectPack который содержит CRUD операции и содержит требуемые экшены.
from objectpack.tree_object_pack.actions import ObjectPack
# Импорт ModelEditWindow для генерации окон редактирования.
from objectpack.ui import ModelEditWindow
# Импорт отображения окон.
from .ui import (ContentTypeListWindow, UserListWindow, UserAddWindow, GroupListWindow,
                 PermissionListWindow, PermissionAddWindow,
                 )


# Определение классов, указание моделей по которым они будут строиться и наборов действий для них.
class ContentTypePack(ObjectPack):
    model = ContentType  # Модель для построения.
    list_window = ContentTypeListWindow  # Отоброжение окна списком объектов.
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)  # Указание на использование окна.
    add_to_menu = True  # Добавление в меню "Пуск".
    add_to_desktop = True  # Добавление на рабочий стол.


class UserPack(ObjectPack):
    model = User
    list_window = UserListWindow
    add_window = edit_window = UserAddWindow  # Использование окна описанного в ручную в ui.py .
    add_to_menu = True
    add_to_desktop = True


class GroupPack(ObjectPack):
    model = Group
    list_window = GroupListWindow
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)
    add_to_menu = True
    add_to_desktop = True


class PermissionPack(ObjectPack):
    model = Permission
    list_window = PermissionListWindow
    add_window = edit_window = PermissionAddWindow  # Использование окна описанного в ручную в ui.py .
    add_to_menu = True
    add_to_desktop = True
