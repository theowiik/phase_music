from typing import List

from pydantic import BaseModel


class ConfigPhaseSchema(BaseModel):
    name: str
    imgs: str
    audio: str


class ConfigEndingSchema(BaseModel):
    key: str
    name: str
    img: str
    audio: str


class ConfigSfxSchema(BaseModel):
    name: str
    key: str
    audio: str


class ConfigSchema(BaseModel):
    phases: List[ConfigPhaseSchema]
    endings: List[ConfigEndingSchema]
    sfx: List[ConfigSfxSchema]
    font: str
