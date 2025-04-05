from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from .database import Base

class Operadora(Base):
    __tablename__ = "operadoras_de_plano_de_saude_ativas"
    
    id = Column(Integer, primary_key=True, index=True)
    registro_ans = Column(Integer, nullable=False, unique=True)
    cnpj = Column(String(14), nullable=False, unique=True)
    razao_social = Column(String(255), nullable=False)
    nome_fantasia = Column(String(255))
    modalidade = Column(String(255), nullable=False)
    logradouro = Column(String(255), nullable=False)
    numero = Column(String(12), nullable=False)
    complemento = Column(String(255))
    bairro = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    uf = Column(String(2), nullable=False)
    cep = Column(String(8), nullable=False)
    ddd = Column(String(3), nullable=False)
    telefone = Column(String(10), nullable=False)
    fax = Column(String(10))
    endereco_eletronico = Column(String(255), nullable=False)
    representante = Column(String(255), nullable=False)
    cargo_representante = Column(String(255), nullable=False)
    regiao_de_comercializacao = Column(String(255), nullable=False)
    data_registro_ans = Column(Date, nullable=False)

class Demonstracoes(Base):
    __tablename__ = "demonstracoes_contabeis"
    
    id = Column(Integer, primary_key=True, index=True)
    _data = Column(Date, nullable=False)
    reg_ans = Column(Integer, ForeignKey("operadoras_de_plano_de_saude_ativas.registro_ans"), nullable=False)
    cd_conta_contabil = Column(Integer, nullable=False)
    descricao = Column(String(255))
    vl_saldo_inicial = Column(Float, nullable=False)
    vl_saldo_final = Column(Float, nullable=False)

    operadora = relationship("Operadora")
    
