from pydantic import BaseModel, ConfigDict


class BaseModelAdj(BaseModel):
    model_config: ConfigDict = ConfigDict(
        frozen=True,
        extra="forbid",
    )


class Language(BaseModelAdj):
    id: int
    code: str
    title: str
    title_local: str
    current: bool
    title_short: str
