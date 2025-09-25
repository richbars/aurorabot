from fastapi import APIRouter
from app.api.services.faq_service import get_faqs

router = APIRouter(prefix="/faq", tags=["FAQ"])

@router.get("/")
async def list_faqs():
    return get_faqs()
