from pydantic import BaseModel
from typing import Optional


class CreatePessoa(BaseModel):
    name: str
    phone: str
    sexo: str
    state: str
    namestate: str
    city: str


class UpdatePessoa(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    sexo: Optional[str] = None
    state: Optional[str] = None
    namestate: Optional[str] = None
    city: Optional[str] = None



# class Pessoa: 
#     def __init__(self, name,phone,sexo,state,namestate,city) -> None:
#         self.name = name
#         self.phone = str(phone)
#         self.sexo = sexo
#         self.state = state
#         self.namestate = namestate
#         self.city = city

#     def format_phone(self):
#         self.phone = f"({self.phone[:2]}){self.phone[2:]}"    

# pessoa1 = Pessoa("João",51993566002,"M","RS","Rio Grande","Poa")
# print(pessoa1.phone)
# pessoa1.format_phone()
# print(pessoa1.phone)

# pessoa2 = Pessoa()

