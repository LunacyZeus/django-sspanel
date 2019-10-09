import os

from configs.default import *

DEBUG = False

DATABASES["default"].update(
    {
        "PASSWORD": os.getenv("MYSQL_PASSWORD", "Ho123456@"),
        "HOST": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "USER": os.getenv("MYSQL_USER", "root"),
    }
)
