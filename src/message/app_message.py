from typing import List

from src.utils import BaseModel
from src.socket.buffer import Buffer

class AppMessage(BaseModel):

    id: int
    msg: Buffer
    len_data: int




def parseMsgs(buffer: Buffer) -> List[AppMessage]:
    messages = []
    print(buffer.data)
    while buffer.has_data_left():

        header = buffer.read_n_bytes(2, False)
        id = header >> 2
        if id == 0:
            continue
        len_len_data = header & 0b11
        if len_len_data == 0:
            continue
        len_data = buffer.read_n_bytes(len_len_data, False)
        if len_data == 0:
            continue
        app_msg = AppMessage(id=id, len_data=len_data, msg=buffer.read_n_bytes_buffer(len_data))
        messages.append(app_msg)


    return messages



