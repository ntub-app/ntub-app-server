from config.settings import env

from datetime import timedelta


ACCESS_TOKEN_LIFETIME = env('ACCESS_TOKEN_LIFETIME', cast=float, default=0.25)

REFRESH_TOKEN_LIFETIME = env('REFRESH_TOKEN_LIFETIME', cast=float, default=24)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=ACCESS_TOKEN_LIFETIME),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=REFRESH_TOKEN_LIFETIME),
    'ROTATE_REFRESH_TOKENS': True,
}
