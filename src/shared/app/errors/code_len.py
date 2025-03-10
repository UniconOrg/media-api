from core.utils.logger import logger
from shared.app.errors.base import BaseError
from shared.app.status_code import StatusCodes


class CodeLenError(BaseError):
    external_code = StatusCodes.HTTP_422_UNPROCESSABLE_ENTITY
    internal_code = StatusCodes.APP_CODE_LENGTH

    def __init__(self) -> None:
        self.message = self.__class__.internal_code.description
        super().__init__(self.message)
        logger.error(self.message)
