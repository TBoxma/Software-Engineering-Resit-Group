class CategoryNotFoundException(Exception):
    """Custom exception to indicate that a category with the provided name was not found."""

class TaskNotFoundException(Exception):
    """Custom exception to indicate that a task with the provided name was not found."""