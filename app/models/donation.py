from sqlalchemy import Column, ForeignKey, Integer, Text

from .abstract import CommonFields


class Donation(CommonFields):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
