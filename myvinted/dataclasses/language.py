from myvinted.dataclasses.base import BaseModelAdj


class Language(BaseModelAdj):
    id: int
    code: str
    title: str
    title_local: str
    current: bool
    title_short: str
