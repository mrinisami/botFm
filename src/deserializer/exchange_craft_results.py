from src.protocol.fm_results import FmResults, ObjectEffect, ObjectModified
from src.socket.buffer import Buffer


def deserialize_4294(buffer: Buffer) -> FmResults:
    craft_result = buffer.read_n_bytes(1, False)
    object_gid = buffer.read_var_int()
    effects_len = buffer.read_n_bytes(2, False)
    object_effect = []
    for i in range(effects_len):
        object_effect_id = buffer.read_n_bytes(2, False)
        action_id = buffer.read_var_short()
        object_effect.append(ObjectEffect(object_effect_id=object_effect_id, action_id=action_id))

    object_gid = buffer.read_var_int()
    quantity = buffer.read_var_int()
    magic_pool_status = buffer.read_n_bytes(1, False)

    return FmResults(craft_result=craft_result, object_gid=object_gid, effects_len=effects_len,
                     object_effect=object_effect, quantity=quantity, magic_pool_status=magic_pool_status)


def deserialize_4738(buffer: Buffer):
    position = buffer.read_n_bytes(2, True)
    object_gid = buffer.read_var_int()
    effects_len = buffer.read_n_bytes(2, False)
    object_effect = []
    for i in range(effects_len):
        object_effect_id = buffer.read_n_bytes(2, False)
        action_id = buffer.read_var_short()
        object_effect.append(ObjectEffect(object_effect_id=object_effect_id, action_id=action_id))

    object_uid = buffer.read_var_int()
    quantity = buffer.read_var_int()

    return ObjectModified(position=position, object_uid=object_uid, object_gid=object_gid, object_effect=object_effect,
                        effects_len=effects_len, quantity=quantity)
