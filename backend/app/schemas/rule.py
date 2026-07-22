from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class RuleCreate(BaseModel):
    """Schema for creating a new detection rule."""

    title: str | None = Field(None, max_length=255)
    product: str | None = Field(None, max_length=255)
    condition: str | None = Field(None, max_length=500)
    mitre_mapping: dict[str, Any] | None = None

    model_config = ConfigDict(extra="forbid")


class RuleUpdate(BaseModel):
    """Schema for partial updates to an existing detection rule."""

    title: str | None = Field(None, max_length=255)
    product: str | None = Field(None, max_length=255)
    condition: str | None = Field(None, max_length=500)
    mitre_mapping: dict[str, Any] | None = None

    model_config = ConfigDict(extra="forbid")


class RuleResponse(BaseModel):
    """Schema returned by the API for a persisted rule."""

    id: int
    title: str | None = None
    product: str | None = None
    condition: str | None = None
    mitre_mapping: dict[str, Any] | None = None
    risk_score: int | None = Field(None, ge=0, le=100)
    quality_score: int | None = Field(None, ge=0, le=100)
    validation_status: str | None = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True, extra="forbid")
