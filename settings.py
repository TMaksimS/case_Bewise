from envparse import Env

env = Env()
env.read_envfile(".env")

DB_USER = env.str("DB_USER", default="postgres")
DB_PASS = env.str("DB_PASS", default="postgres")
DB_NAME = env.str("DB_NAME", default="postgres")
DB_HOST = env.str("DB_HOST", default="localhost")


REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
)