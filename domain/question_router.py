from fastapi import APIRouter

from app.database import SessionLocal # db연결하기
from app.models import Question

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list")
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    db.close()
    return _question_list