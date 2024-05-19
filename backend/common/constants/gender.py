from common.constants.base_const import Const

__all__ = ["Genders"]

class Genders(Const):
    Select = 0

    MALE = 0
    FEMALE = 1
    OTHER = 2

    GENDERS = (
        (MALE, "male"),
        (FEMALE, "female"),
        (OTHER, "other"),
    )