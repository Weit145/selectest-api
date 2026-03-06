from app.schemas.vacancy import VacancyCreate, VacancyRead, VacancyUpdate
from app.models.vacancy import Vacancy

from typing import Optional,List

def db_to_read_vacancy(vacancy_db:Optional[Vacancy])->Optional[VacancyRead]:
    if vacancy_db is None:
        return None
    return VacancyRead.model_validate(vacancy_db)

def list_db_to_read_vacancy(vacancy_db: Optional[List[Vacancy]]) -> List[VacancyRead]:
    if vacancy_db is None:
        return []
    return [VacancyRead.model_validate(v) for v in vacancy_db]