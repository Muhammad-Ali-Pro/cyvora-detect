from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, JSON, String

from backend.app.database.database import Base


class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=True)
    product = Column(String(255), nullable=True)
    condition = Column(String(500), nullable=True)
    mitre_mapping = Column(JSON, nullable=True)
    risk_score = Column(Integer, nullable=True)
    quality_score = Column(Integer, nullable=True)
    validation_status = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
