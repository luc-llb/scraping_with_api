from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from . import models, schemas
from .database import engine, get_db

from fastapi.middleware.cors import CORSMiddleware

# Create the database tables
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # URL of frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""CRUD operations for Operadora"""
@app.get("/operadoras/", response_model=List[schemas.Operadora])
def read_operadoras(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    operadoras = db.query(models.Operadora).offset(skip).limit(limit).all()
    return operadoras

# Get by CNPJ
@app.get("/operadoras/cnpj/{cnpj}", response_model=schemas.Operadora)
def read_operadora_by_cnpj(cnpj: str, db: Session = Depends(get_db)):
    operadora = db.query(models.Operadora).filter(models.Operadora.cnpj == cnpj).first()
    if operadora is None:
        raise HTTPException(status_code=404, detail="Operadora not found")
    return operadora

# Get by Registro ANS
@app.get("/operadoras/registro_ans/{registro_ans}", response_model=schemas.Operadora)
def read_operadora_by_registro_ans(registro_ans: int, db: Session = Depends(get_db)):
    operadora = db.query(models.Operadora).filter(models.Operadora.registro_ans == registro_ans).first()
    if operadora is None:
        raise HTTPException(status_code=404, detail="Operadora not found")
    return operadora

# Get by Nome Fantasia
@app.get("/operadoras/nome_fantasia/{nome_fantasia}", response_model=schemas.Operadora)
def read_operadora_by_nome_fantasia(nome_fantasia: str, db: Session = Depends(get_db)):
    operadora = db.query(models.Operadora).filter(models.Operadora.nome_fantasia == nome_fantasia).first()
    if operadora is None:
        raise HTTPException(status_code=404, detail="Operadora not found")
    return operadora

# Get by endereco_eletronico
@app.get("/operadoras/endereco_eletronico/{endereco_eletronico}", response_model=schemas.Operadora)
def read_operadora_by_endereco_eletronico(endereco_eletronico: str, db: Session = Depends(get_db)):
    operadora = db.query(models.Operadora).filter(models.Operadora.endereco_eletronico == endereco_eletronico).first()
    if operadora is None:
        raise HTTPException(status_code=404, detail="Operadora not found")
    return operadora

# Get by modalidade
@app.get("/operadoras/modalidade/{modalidade}", response_model=List[schemas.Operadora])
def read_operadora_by_modalidade(modalidade: str, db: Session = Depends(get_db)):
    operadoras = db.query(models.Operadora).filter(models.Operadora.modalidade == modalidade).limit(10).all()
    if not operadoras:
        raise HTTPException(status_code=404, detail="Operadora not found")
    return operadoras

# Get by data_registro_ans
@app.get("/operadoras/data_registro_ans/{data_registro_ans}", response_model=List[schemas.Operadora])
def read_operadora_by_data_registro_ans(data_registro_ans: str, db: Session = Depends(get_db)):
    try:
        data = datetime.strptime(data_registro_ans, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de data inválido. Use AAAA-MM-DD.")

    operadoras = db.query(models.Operadora).filter(models.Operadora.data_registro_ans == data).limit(10).all()
    
    if not operadoras:
        raise HTTPException(status_code=404, detail="Nenhuma operadora encontrada com essa data.")

    return operadoras

@app.post("/operadoras/", response_model=schemas.Operadora)
def create_operadora(operadora: schemas.OperadoraCreate, db: Session = Depends(get_db)):
    db_operadora = models.Operadora(**operadora.dict())
    db.add(db_operadora)
    db.commit()
    db.refresh(db_operadora)
    return db_operadora

@app.put("/operadoras/{operadora_id}", response_model=schemas.Operadora)
def update_operadora(operadora_id: int, operadora: schemas.OperadoraCreate, db: Session = Depends(get_db)):
    db_operadora = db.query(models.Operadora).filter(models.Operadora.id == operadora_id).first()
    if db_operadora is None:
        raise HTTPException(status_code=404, detail="Operadora not found")
    for key, value in operadora.dict().items():
        setattr(db_operadora, key, value)
    db.commit()
    db.refresh(db_operadora)
    return db_operadora

@app.delete("/operadoras/{operadora_id}")
def delete_operadora(operadora_id: int, db: Session = Depends(get_db)):
    db_operadora = db.query(models.Operadora).filter(models.Operadora.id == operadora_id).first()
    if db_operadora is None:
        raise HTTPException(status_code=404, detail="Operadora not found")
    db.delete(db_operadora)
    db.commit()
    return {"detail": "Operadora deleted"}