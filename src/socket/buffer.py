from __future__ import annotations

from src.utils import BaseModel


class BufferException(Exception):
    pass


class Buffer(BaseModel):

    data: str
    pos: int
    int_size = 32
    mask_128 = 0b10000000
    mask_127 = 0b01111111
    chunk_bit_size = 7
    short_size = 16
    short_max_value = 32767
    unsigned_short_max_value = 65536

    @staticmethod
    def from_str(data: str):
        return Buffer(data=data, pos=0)

    def read_n_bytes(self, n : int, signed: bool) -> int:
        self.__validate_read_bytes(n * 2)
        start_pos = self.pos
        self.pos += n * 2
        return int.from_bytes(bytes.fromhex(self.data[start_pos:self.pos]), "big", signed=signed)

    def read_n_bytes_buffer(self, n: int) -> Buffer:
        self.__validate_read_bytes(n * 2)
        start_pos = self.pos
        self.pos += n * 2
        return Buffer.from_str(self.data[start_pos: self.pos])

    def read_var_int(self) -> int:
        ans = 0
        for i in range(0, 32, 7):
            b = self.read_n_bytes(1, False)
            ans += (b & 0b01111111) << i
            if not b & 0b10000000:
                return ans

    def read_var_short(self) -> int:
        ans = 0
        for i in range(0, 16, 7):
            b = self.read_n_bytes(1, True)
            ans += (b & 0b01111111) << i
            if not b & 0b10000000:
                return ans

    def has_data_left(self) -> bool:
        return len(self.data) > self.pos

    def __validate_read_bytes(self, n: int):
        if n + self.pos > len(self.data):
            raise BufferException("You've reached the end of the buffer")

    def read_signed_bytes(self, n: int) -> int:
        self.__validate_read_bytes(n * 2)

    def __repr__(self):
        return self.data