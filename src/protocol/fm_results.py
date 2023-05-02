from typing import List
from src.utils import BaseModel


class ObjectEffect(BaseModel):
    action_id: int
    object_effect_id: int


class FmResults(BaseModel):

    craft_result: int
    object_gid: int
    effects_len: int
    object_effect: List[ObjectEffect]
    quantity: int
    magic_pool_status: int


class ObjectModified(BaseModel):

    position: int
    object_gid: int
    effects_len: int
    object_effect: List[ObjectEffect]
    quantity: int
    object_uid: int


