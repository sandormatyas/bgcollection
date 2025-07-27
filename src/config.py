from os import getenv

import flet as ft
from dynaconf import Dynaconf


def add_dynamic_vars(settings):
    data = {
        "BLACK_SEMI_TRANSPARENT": ft.Colors.BLACK54,
        "TEXT_COLOR": ft.Colors.WHITE,
        "APP_DATA_PATH": getenv("FLET_APP_STORAGE_DATA"),
        "APP_TEMP_PATH": getenv("FLET_APP_STORAGE_TEMP"),
        "DB_URL": f"sqlite:///{getenv('FLET_APP_STORAGE_DATA')}/bgcollection.db",
    }
    return data


settings = Dynaconf(settings_files=["settings.toml"], post_hooks=add_dynamic_vars)
