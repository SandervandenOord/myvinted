from pydantic import BaseModel, ConfigDict


class BaseModelAdj(BaseModel):
    model_config: ConfigDict = ConfigDict(
        frozen=True,
        extra="forbid",
    )


class ApiUrl(BaseModelAdj):
    base: str
    languages: str
    events_feed: str
    users: str
    items: str


class Config(BaseModelAdj):
    api_url: ApiUrl


class Language(BaseModelAdj):
    id: int
    code: str
    title: str
    title_local: str
    current: bool
    title_short: str
