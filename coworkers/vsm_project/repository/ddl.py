from functools import wraps
from .models import User, Procedure
from py_logger import get_logger

logger = get_logger(__name__)


def is_exist_user(user_id):
    """Функція перевірки унікальності юзера"""
    user = User.objects(user_id=user_id)
    if user:
        return True
    else:
        return False


def set_user(user_id, first_name, last_name):
    """Функція запису юзерів в БД"""
    user = User(user_id=user_id, first_name=first_name, last_name=last_name)
    user.save()
    logger.info(f'User: {first_name} {last_name} was created.')


def set_procedure(title, image_url, desc_url):
    """Функція запису процедур в БД"""
    procedure = Procedure(title=title, image_url=image_url, desc_url=desc_url)
    procedure.save()
    logger.info(f'Procedure {title} was added')


def get_procedures():
    """Функція отримання усіх процедур"""
    procedures = Procedure.objects.all()
    return procedures


if __name__ == '__main__':
    # title = 'ИНЪЕКЦИОННАЯ СКЛЕРОТЕРАПИЯ СОСУДОВ НОГ'.capitalize()
    # image_url = 'http://vsm-skinlaser.com.ua/files/product/3/3/3.jpg'
    # desc_url = 'http://vsm-skinlaser.com.ua/product/skleroterapiya-ven--sosudistyh-setochek---040-zvezdochek--pauchkov--041--na-nogah'
    # set_procedure(title, image_url, desc_url)
    pass
