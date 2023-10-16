from fastapi import APIRouter, Request
from typing import Annotated
from db import absences

router = APIRouter(prefix="/absences")

@router.post('/')
async def create_absence(req: Request):
    form = await req.form()
    absences.create_absence(form.get('user_id'), form.get('from'), form.get('to'))
    return form

@router.get('/')
async def get_all_absences():
    return absences.get_all_absences()
