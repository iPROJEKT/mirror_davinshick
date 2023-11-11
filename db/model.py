from sqlalchemy import Column, String, Integer, CheckConstraint, Boolean
from sqlalchemy_utils import ChoiceType

from .base import Base
from .const import MAX_LEIGHT_NAME, MAX_LEIGHT_DESCRIPTION, MAX_LEIGHT_GENDER


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class User(Base):
    __table_args__ = (
        CheckConstraint(
            'age > 0',
        ),
    )
    name = Column(
        String(
            MAX_LEIGHT_NAME
        ),
        nullable=False
    )
    last_name = Column(
        String(
            MAX_LEIGHT_NAME
        ),
        nullable=False
    )
    age = Column(
        Integer,
        nullable=False
    )
    photo = Column(
        String,
        nullable=False
    )
    description = Column(
        String(
            MAX_LEIGHT_DESCRIPTION
        )
    )
    gender = ChoiceType(
        GENDER_CHOICES,
        impl=String(
            length=MAX_LEIGHT_GENDER
        )
    )
    active = Column(
        Boolean
    )
    full_profile = Column(
        Boolean
    )


class Choices(Base):
    user_id = Column(
        Integer
    )
    like = Column(
        Boolean
    )


class UserFavorite(Base):
    first_user = Column(
        Integer
    )
    second_user = Column(
        Integer
    )
    like = Column(
        Boolean
    )
