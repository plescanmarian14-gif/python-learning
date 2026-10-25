from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from typing import List,Optional
from sqlalchemy import or_
from app.database import get_db
from app.models import ArticoleModel
from app.schemas import ArticoleCreate,ArticoleResponse

router=APIRouter(
    prefix="/articole",
    tags=["Articole SQL"]
)

@router.post("",response_model=ArticoleResponse,status_code=status.HTTP_201_CREATED)
def verificare(
        cod_bare:ArticoleCreate,
        db:Session=Depends(get_db)
):
   articol=db.query(ArticoleModel).filter(ArticoleModel.cod_bare==articol_in.cod_bare).first()
   if articol:
       raise HTTPException(status_code=400,detail="Codul exista")
   db_articol=ArticoleModel(**cod_bare.model_dump())
   db.add(db_articol)
   db.commit()
   db.refresh(db_articol)

   return db_articol

@router.get("")
def cautare(
    q:Optional[str]=None,
    doar_in_stoc:Optional[bool]=None,
    db:Session=Depends(get_db),
    sortare:Optional[str]=None,
):
    query=db.query(ArticoleModel)
    if q:
        termen = f"%{q}%"
        query = query.filter(
            or_(
                ArticoleModel.nume.ilike(termen),
                ArticoleModel.cod_bare.ilike(termen)
            )
        )
    query=db.query(ArticoleModel)
    if doar_in_stoc:
        query=query.filter(ArticoleModel.stoc>0)
    if sortare=="pret":
        q=query.order_by(ArticoleModel.pret.asc())
    return q.all()

@router.get("/{articol_id")
def caut(articol_id:int,
         db:Session=Depends((get_db)
                            )
         ):
    articol=db.query(ArticoleModel).filter(ArticoleModel.id==articol_id).first()
    if not articol:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND,detail=f"Articol negasit")
    return articol

@router.put("/{articol_id}",response_model=ArticoleCreate)
def actualizare(
        articol_id:int,
        articol_in:ArticoleCreate,
        db:Session=Depends(get_db)
):
    db_articol=db.query(ArticoleModel).filter(ArticoleModel.id==articol_id).first()
    if not db_articol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            details="Articol negasit")
    if articol_in.cod_bare!=db_articol.cod_bare:
        cod_existent=db.query(ArticoleModel).filter(ArticoleModel.cod_bare==articole_in.cod_bare,ArticoleModel.id!=articol_id).first()
        if cod_existent:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Exsita deja"
            )
    date_noi=articol_in.model_dump()
    for key,value in date_noi.items():
        setattr(db_articol,key,value)
    db.commit()
    db.refresh(db_articol)
    return db_articol

@router.delete("/{articol_id}",status_code=status.HTTP_200_OK)
def stergere_articol(
        articol_id:int,
        db:Session=Depends(get_db)
):
    articol=db.query(ArticoleModel).filter(ArticoleModel.id==articol_id).filter()
    if articol:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Articol negasit"
        )
    db.delete(articol)
    db.commit()
    return f"Articolul {articol} a fost sters"