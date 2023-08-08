# Импорт базового окна редактирования, базового окна списка обьектов и модуля создающего(возвращающего)ExtComboBox.
from objectpack.ui import BaseEditWindow, BaseListWindow, make_combo_box
# Импорт встроенных моделей Django.
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
# Импорт модуля со всеми компонентами пользовательского интерфейса. Взято из примера в документации.
from m3_ext.ui import all_components as ext


# Определение окон для отображения, создания и редактирования объектов.
class ContentTypeListWindow(BaseListWindow):
    model = ContentType  # модель для построения списка объектов.


class UserListWindow(BaseListWindow):
    model = User


class UserAddWindow(BaseEditWindow):  # Окно создания/редактирования пользователя(по примеру из документации)

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:self.
        """
        super(UserAddWindow, self)._init_components()
        # Использование импортированного модуля для создания интерфейса.
        self.field__username = ext.ExtStringField(
            label=u'Имя пользователя',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'E-mail',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'Имя',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'Фамилия',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'Администратор',
            name='is_superuser',
            anchor='100%',
            checked=False
        )

        self.field__is_staff = ext.ExtCheckBox(
            label=u'Персонал',
            name='is_staff',
            anchor='100%',
            checked=False
        )

        self.field__is_active = ext.ExtCheckBox(
            label=u'Активный',
            name='is_active',
            anchor='100%',
            checked=True
        )

        self.field__last_login = ext.ExtDateField(
            label=u'Последний вход',
            name='last_login',
            anchor='100%',
            format='d.m.Y'
        )

        self.field__date_joined = ext.ExtDateField(
            label=u'Дата регистрации',
            name='date_joined',
            anchor='100%',
            format='d.m.Y'
        )

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__email,
            self.field__first_name,
            self.field__last_name,
            self.field__is_superuser,
            self.field__is_staff,
            self.field__is_active,
            self.field__last_login,
            self.field__date_joined
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class GroupListWindow(BaseListWindow):
    model = Group


class PermissionListWindow(BaseListWindow):
    model = Permission


class PermissionAddWindow(BaseEditWindow):  # Окно создания/редактирования разрешений(по примеру из документации и
    # скриншотов из задания)

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:self.
        """
        super(PermissionAddWindow, self)._init_components()
        self.field__name = ext.ExtStringField(
            label=u'Название',
            name='name',
            allow_blank=False,
            anchor='100%'
        )

        content_types = ContentType.objects.all()  # Получение всех доступных типов контента из модели
        content_type_choices = [(ct.id, ct.name) for ct in content_types]  # Создание списка в котором каждый элемент
        # это кортеж. Этот список используется для создания выпадающего списка в диалоговом окне.
        # Вызов функции make_combo_box.
        self.field__content_type = make_combo_box(
            label=u'Тип контента',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=content_type_choices,  # Список данных которые отображаютя в выпадающем списке.
            display_field='name',
        )

        self.field__codename = ext.ExtStringField(
            label=u'Кодовое имя',
            name='codename',
            allow_blank=False,
            anchor='100%'
        )

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        """
        Установка параметров окна
        :params: Словарь с параметрами, передается из пака
        """
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'
