from sqlalchemy import Column, String, Text

from .abstract import CommonFields


class CharityProject(CommonFields):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return self.name
