from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DOCS_", env_file=".env")

    data_dir: Path = Path("./data")
    model: str = "BAAI/bge-small-en-v1.5"
    api_key: str | None = None
    chunk_words: int = 260
    chunk_overlap_words: int = 40
    max_upload_mb: int = 100
