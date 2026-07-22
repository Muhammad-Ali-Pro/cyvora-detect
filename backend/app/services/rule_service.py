from __future__ import annotations

from backend.app.models.rule import Rule
from backend.app.repositories.rule_repository import RuleRepository
from backend.app.schemas.rule import RuleCreate, RuleUpdate


class RuleNotFoundError(Exception):
    """Raised when a requested rule does not exist."""


class RuleService:
    """Application service for managing rules."""

    def __init__(self, repository: RuleRepository) -> None:
        self._repository = repository

    def create_rule(self, rule_data: RuleCreate) -> Rule:
        """Create a new rule using the repository."""
        payload = rule_data.model_dump(exclude_none=True)
        return self._repository.create_rule(payload)

    def get_rule(self, rule_id: int) -> Rule:
        """Return a rule by its identifier or raise if not found."""
        rule = self._repository.get_rule(rule_id)
        if rule is None:
            raise RuleNotFoundError(f"Rule with id {rule_id} was not found")
        return rule

    def get_all_rules(self) -> list[Rule]:
        """Return all persisted rules."""
        return self._repository.list_rules()

    def update_rule(self, rule_id: int, rule_data: RuleUpdate) -> Rule:
        """Update an existing rule using the repository."""
        payload = rule_data.model_dump(exclude_none=True)
        rule = self._repository.update_rule(rule_id, payload)
        if rule is None:
            raise RuleNotFoundError(f"Rule with id {rule_id} was not found")
        return rule

    def delete_rule(self, rule_id: int) -> bool:
        """Delete a rule by its identifier or raise if it does not exist."""
        deleted = self._repository.delete_rule(rule_id)
        if not deleted:
            raise RuleNotFoundError(f"Rule with id {rule_id} was not found")
        return True
