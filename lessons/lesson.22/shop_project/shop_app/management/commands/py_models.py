from dataclasses import dataclass
from datetime import datetime


@dataclass
class FooBar:
    spam: str
    eggs: str
    created_at: datetime
    tags: tuple[str, ...]
