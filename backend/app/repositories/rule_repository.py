from typing import List, Optional
from sqlalchemy.orm import Session

from backend.app.models.rule import Rule
from backend.app.database.database import SessionLocal


class RuleRepository:
    def __init__(self, session: Optional[Session] = None):
        self.session = session or SessionLocal()

    def create_rule(self, rule_data: dict) -> Rule:
        rule = Rule(**rule_data)
        self.session.add(rule)
        self.session.commit()
        self.session.refresh(rule)
        return rule

    def get_rule(self, rule_id: int) -> Optional[Rule]:
        return self.session.query(Rule).filter(Rule.id == rule_id).first()

    def list_rules(self) -> List[Rule]:
        return self.session.query(Rule).order_by(Rule.created_at.desc()).all()

    def delete_rule(self, rule_id: int) -> bool:
        rule = self.get_rule(rule_id)
        if not rule:
            return False

        self.session.delete(rule)
        self.session.commit()
        return True
