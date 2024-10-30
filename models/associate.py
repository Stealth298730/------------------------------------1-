from sqlalchemy import Column, String, ForeignKey, Table

from models.base import Base


tuor_ingred_assoc_table = Table(
    "tuor_ingred_assoc_table",
    Base.metadata,
    Column("tuor_id", ForeignKey("tuors.id"), primary_key=True),

)