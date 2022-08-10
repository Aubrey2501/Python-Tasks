from dataclasses import dataclass
from enum import Enum


@dataclass(unsafe_hash=True)
class Hotel:
	name: str = None
	address: str = None
	center_dist: float = None
	cost: float = None
	photos: list[str] = None
	link: str = None


	