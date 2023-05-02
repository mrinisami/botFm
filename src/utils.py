from pydantic import BaseModel as PyBaseModel


class BaseModel(PyBaseModel):
    class Config:
        arbitrary_types_allowed = True


bytes_to_read = {"unsigned_byte": 1, "unsigned_short": 2, "unsigned_int": 4, "int": 4, "short": 2, "read_byte": 1}


