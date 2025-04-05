from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schemas for Operadora
class OperadoraBase(BaseModel):
    registro_ans: int
    cnpj: str
    razao_social: str
    nome_fantasia: str
    modalidade: str
    logradouro: str
    numero: str
    complemento: Optional[str] = None
    bairro: str
    cidade: str
    uf: str
    cep: str
    ddd: str
    telefone: str
    fax: Optional[str] = None
    endereco_eletronico: str
    representante: str
    cargo_representante: str
    regiao_de_comercializacao: str
    data_registro_ans: datetime

class OperadoraCreate(OperadoraBase):
    pass

class Operadora(OperadoraBase):
    id: int
    
    class Config:
        orm_mode = True

# Schemas for Demonstracao
class DemonstracaoBase(BaseModel):
    _data: datetime
    reg_ans: int
    cd_conta_contabil: int
    vl_saldo_inicial: float
    vl_saldo_final: float
    descricao: Optional[str] = None

class DemonstracaoCreate(DemonstracaoBase):
    pass

class Demonstracao(DemonstracaoBase):
    id: int
    
    class Config:
        orm_mode = True