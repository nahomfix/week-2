from pathlib import Path


class Config:
    ROOT_DIR = Path.cwd().parent
    DATA_PATH = (ROOT_DIR / "data").resolve()
    MODELS_PATH = (ROOT_DIR / "data").resolve()


# DATA_PATH = (ROOT_DIR / "data").resolve()
