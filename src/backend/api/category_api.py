from database.session_wrapper import query
from src.backend.api.base_api import BaseModelApi
from src.backend.model.category import Category

from sqlalchemy.orm import Session


class CategoryApi(BaseModelApi):
    """
    API class for performing operations related to Category model.
    Inherits from BaseModelApi for common CRUD operations.
    """
    def __init__(self) -> None:
        super().__init__(Category)
