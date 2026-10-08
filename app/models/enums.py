"""Defines the enums for some of our cost_items."""

from enum import Enum

class CostCategory(str, Enum):
    TRANSPORT = "transport"
    ACCOMMODATION = "accommodation"
    FOOD = "food"
    ACTIVITIES = "activities"
    OTHER = "other"

class TimeBasis(str, Enum):
    ONE_OFF = "one_off"
    PER_DAY = "per_day"
    PER_NIGHT = "per_night"

class TravellerBasis(str, Enum):
    SHARED = "shared"
    PER_PERSON = "per_person"