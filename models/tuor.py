from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from models.base import Base
from models.associate import tuor_ingred_assoc_table


class Tuor(Base):
    __tablename__ = "tuors"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column()
