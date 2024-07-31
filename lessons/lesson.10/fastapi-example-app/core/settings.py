from os import getenv
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "db.sqlite3"

DB_URL = getenv('DATABASE_URL', f"sqlite+aiosqlite:///{DB_PATH}")
CURRENT_SETTINGS = getenv('SETTINGS', 'Settings')

print('OUR DB URL', DB_URL)


class Settings(BaseSettings):
    # db_url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    # db_url: str = f"postgresql+asyncpg://pguser:dieneu38dmN@localhost/shop"
    # db_url: str = f"postgresql+asyncpg://pguser:dieneu38dmN@pg/shop"

    db_url: str = DB_URL
    # echo: bool = False
    echo: bool = True


class TestSettings(BaseSettings):
    db_url: str = DB_URL
    # echo: bool = False
    echo: bool = False


class ProdSettings(TestSettings):
    pass


settings_dict = {
    'Settings': Settings,
    'TestSettings': TestSettings
}


settings = settings_dict.get(CURRENT_SETTINGS, Settings)()
