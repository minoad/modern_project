from dataclasses import dataclass


@dataclass()
class Command:
    name: str

    def __post_init__(self):
        self.name = self.name.lower()
