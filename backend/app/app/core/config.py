import os


def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result


API_V1_STR = "/api/v1"

SECRET_KEY = os.getenvb(b"SECRET_KEY")

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

CONFERENCE_LIST = {"CVPR", "ICCV", "ACCV", "ECCV", "NIPS", "NEURIPS", "SIGGRAPH", "AAAI", "ICML", "IJCAI"}

DB_DRIVER = os.getenv("DB_DRIVER")
DB_SERVER = os.getenv("DB_SERVER")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
if DB_DRIVER == "sqlite":
    SQLALCHEMY_DATABASE_URI = f"{DB_DRIVER}:///{DB_NAME}"
else:
    SQLALCHEMY_DATABASE_URI = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"

# a string of origins separated by commas, e.g: "http://localhost, http://localhost:4200, http://localhost:3000 "
BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS")

FIRST_SUPERUSER = os.getenv("FIRST_SUPERUSER")
FIRST_SUPERUSER_EMAIL = os.getenv("FIRST_SUPERUSER_EMAIL")
FIRST_SUPERUSER_PASSWORD = os.getenv("FIRST_SUPERUSER_PASSWORD")

USERS_OPEN_REGISTRATION = getenv_boolean("USERS_OPEN_REGISTRATION")