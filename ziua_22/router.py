from http.client import HTTPException

from starlette.middleware.sessions import Session


@router.delete("/clase/{clasa_id}")
def stergere(clasa_in:int,db:Session=Depends(get_db)):
    clasa=db.query(ClasaModel).filter(ClasaModel.id==clasa_in.id).first()

    if not clasa:
        raise HTTPException(status_code=404,detail="CLasa nu exista")
    db.delete(clasa)
    db.commit()
    return {"mesaj":"clasa cu totii copii!"}