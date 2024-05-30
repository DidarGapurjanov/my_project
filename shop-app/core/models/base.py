from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr
from utils import camel_to_snake_case
from sqlalchemy import MetaData
from core.config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_to_snake_case(cls.__name__)}s"
