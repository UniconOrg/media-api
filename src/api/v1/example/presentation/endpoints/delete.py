from uuid import UUID

from fastapi import status

from core.utils.logger import logger
from core.utils.responses import (
    EnvelopeResponse,
)

from .routers import router


@router.delete(
    "/{id}",
    summary="elimina un usuario",
    status_code=status.HTTP_200_OK,
    response_model=EnvelopeResponse,
)
async def delte(
    id: UUID,
):
    logger.info("Delete User")
