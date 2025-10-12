from PyQt5.QtCore import QSettings
from pathlib import Path

_ORG = "Graphene_Sampler_KazuApp"
_APP = "Graphene_Sampler_KazuApp_v1"


def _s():
    return QSettings(_ORG, _APP)


def store_database_path(path):
    _s().setValue("database_path", path)


def load_database_path() -> Path:
    return _s().value("database_path", "", type=str)
