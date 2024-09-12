from typing import Annotated
from pydantic import EmailStr, Field


def base_annotation(field: str, type: type | Annotated = str, optional: bool = False) -> Annotated:
    if optional:
        return Annotated[type | None, Field(description=f"The {field.lower()} of the talent", title=field.title())]
    return Annotated[type, Field(description=f"The {field.lower()} of the talent", title=field.title())]


name_annotation = base_annotation("name")
email_annotation = base_annotation("email", optional=True, type=EmailStr)
id_annotation = base_annotation("id", optional=True, type=int)
linkedIn_annotation = base_annotation("linkedIn", optional=True)
programming_languages_annotation = base_annotation("programming languages", type=list[str])
frameworks_annotation = base_annotation("frameworks", type=list[str])

