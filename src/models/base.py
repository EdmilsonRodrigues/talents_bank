from models.annotations import id_annotation, name_annotation, email_annotation, linkedIn_annotation, programming_languages_annotation, frameworks_annotation
from pydantic import BaseModel


class TalentRequest(BaseModel):
    name: name_annotation  # type: ignore
    email: email_annotation = None  # type: ignore
    linkedIn: linkedIn_annotation = None  # type: ignore
    programming_languages: programming_languages_annotation = []  # type: ignore
    frameworks: frameworks_annotation = []  # type: ignore


class Talent(TalentRequest):
    id: id_annotation = None
