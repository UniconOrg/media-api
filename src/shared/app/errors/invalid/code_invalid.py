from core.utils.logger import logger
from shared.app.errors.base import BaseError
from shared.app.status_code import StatusCodes


class CodeInvalidError(BaseError):
    http_code = StatusCodes.HTTP_404_NOT_FOUND
    internal_code = StatusCodes.APP_INVALID_CODE

    def __init__(self, code: str, operation: str = "verify") -> None:
        self.message = f"The code: {code} is invalid by operation: {operation}"
        super().__init__(self.message)
        logger.error(self.message)
