from uuid import uuid1
from task import Task


class User:
    def __init__(self, name, username, password):
        self.user_id = str(uuid1())
        self.name = name
        self.username = username
        self.password = password

    def to_dict(self) -> dict:
        return {
            'user_id': self.user_id,
            'name': self.name,
            'username': self.username,
            'password': self.password,
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        user = cls(data['name'], data['username'], data['password'])
        user.user_id = data['user_id']
        return user
    
    def add_task(self, task: Task):
        self.tasks.append(task)
    
    def get_tasks(self) -> list[Task]:
        return self.tasks
    
    def get_pending_tasks(self) -> list[Task]:
        return [task for task in self.tasks if not task.completed]
    
    def get_completed_tasks(self) -> list[Task]:
        return [task for task in self.tasks if task.completed]