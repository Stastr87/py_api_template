"""Executable point"""

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sslify import SSLify

from api_extension import open_api
from env.flask_config import set_custom_config
from src.hashmap.password_hash_map import UserPasswordHashMap

app = Flask(__name__)
open_api.init_app(app)

# set custom config placed in env/flask_config.py
set_custom_config(app)

# allow CORS for all domains on all routes.
# Заголовки CORS: используйте заголовки Cross-Origin Resource Sharing (CORS),
# чтобы контролировать, какие домены могут получить доступ к вашему API.
# Это поможет предотвратить выполнение запросов неавторизованными доменами
# и повысит общую безопасность.
cors = CORS(app)

# Flask-JWT-Extended, обеспечивает эффективное решение для
# аутентификации на основе токенов в приложениях Flask.
# JWTManager конфигурируется с секретным ключом,
# а к конечной точке применяется декоратор @jwt_required(),
# гарантирующий, что будут допущены только запросы,
# содержащие действительный JWT.
# Функция get_jwt_identity() (из пакета flask_jwt_extended )
# извлекает идентификатор (информацию о пользователе) из токена,
# предоставляя доступ к конкретным данным пользователя в
# защищенной конечной точке.
#
# Для повышения безопасности периодически меняйте секретный ключ JWT.
# Кроме того, рассмотрите возможность введения времени истечения срока действия токена,
# чтобы минимизировать потенциальное воздействие взломанных токенов.
# Flask-JWT-Extended предлагает гибкую настройку истечения
# срока действия токенов, обеспечивая надежный подход к управлению токенами.
jwt = JWTManager(app)


@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    """
    Автоматически добавляет claims в каждый создаваемый access токен
    identity - это то, что передали в create_access_token(identity=...)
    """
    users_db = UserPasswordHashMap()
    users_db.load_credentials()
    user = users_db.get(identity)
    if user:
        return {
            "role": user.role.value,
        }
    return {}


# Расширение Flask-SSLify – это простой способ реализовать HTTPS в
# приложении Flask.
# При использовании в приложении оно автоматически перенаправляет все
# HTTP-запросы на их HTTPS-аналоги, обеспечивая безопасное взаимодействие
# между клиентами и сервером.
# Благодаря внедрению HTTPS, конфиденциальные данные,
# передаваемые во время API-запросов, такие как токены аутентификации
# или учетные данные пользователей – шифруются,
# что снижает риск перехвата и фальсификации данных.
#
# Дополнительно настройте серверную среду для включения HTTPS на
# уровне сервера,
# используя действительный сертификат SSL/TLS.
# Это расширение дополняет конфигурации на уровне сервера,
# повышая общую безопасность вашего Flask API.
sslify = SSLify(app)

app.run("127.0.0.1", debug=True, port=5555)
