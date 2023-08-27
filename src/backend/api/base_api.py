from typing import List
from database.session_wrapper import query
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.backend.exception import CategoryNotFoundException, TaskNotFoundException

from src.backend.model.category import Category
from src.backend.model.task import Task

class BaseModelApi:
    """
    Base API class for adding, updating, deleting, and retrieving either Categories of Tasks.
    """

    def __init__(self, model: Category | Task) -> None:
        """
        Initializes the BaseModelApi with the provided model (Category or Task).

        :param model: An instance of Category or Task.
        """
        self.model: Category | Task = model
    
    @classmethod
    @query
    def add(cls, name: str, session: Session):
        """
        Adds a new instance of the model to the database.

        :param name: The name attribute of a model.
        :returns: id of created object
        """
        model: Category | Task = cls().model(name=name)

        session.add(model)
        session.commit()

    @classmethod
    @query
    def list_all(cls, session: Session) -> list[Category] | list[Task]:
        return session.scalars(select(cls().model)).all()

    @classmethod
    @query
    def update_by_name(cls, name: str, new_name: str, session: Session):
        """
        Updates the name of an existing model instance based on its name.

        :param name: The new name for the model.
        """
        model: Category | Task = cls()._get_model_by_name(name, session)

        model.name = new_name
        session.commit()
    
    @classmethod
    @query
    def delete_by_name(cls, name: str, session: Session):
        """
        Deletes a model instance by its name and clears related relationships if applicable.

        :param name: The name of the model.
        """
        model: Category | Task = cls()._get_model_by_name(name, session)
        
        if type(model) is Category:
            model.tasks.clear()
        else:
            model.categories.clear()
            model.durations.clear()
        
        session.delete(model)
        session.commit() 
    
    @classmethod
    @query
    def get_by_name(cls, name: str, session: Session) -> Category | Task:
        """
        Retrieves a model instance by its name.

        :param name: The name of the model.
        :returns: An instance of Category or Task.
        :raises: CategoryNotFoundException: If the category with the given name is not found.
        :raises: TaskNotFoundException: If the task with the given name is not found.
        """
        return cls()._get_model_by_name(name, session)
    
    def _get_model_by_name(self, name: str, session: Session) -> Category | Task:
        """
        Retrieves a model instance by its name.

        :param name: The name of the model.
        :returns: An instance of Category or Task.
        """
        if self.model is Category:
            category: Category = session.scalar(select(Category).where(Category.name == name))
            if not category:
                raise CategoryNotFoundException(f"Category with name '{name}' was not found")
            
            return category
        
        elif self.model is Task:
            task: Task = session.scalar(select(Task).where(Task.name == name))

            if not task:
                raise TaskNotFoundException(f"Task with name '{name}' was not found")
            
            return task
        
        else:
            raise Exception(f"Unexpected exeption, class model is of wrong type '{type(self.model)}'")