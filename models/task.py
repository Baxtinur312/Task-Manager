from datetime import datetime
from typing import Optional
from utils import print_satatus

class Task:
    def __init__(self, title: str, description: str = "", deadline: Optional[str] = None):
        self.title = title
        self.description = description
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.deadline = deadline
        self.completed = False
    
    def mark_as_completed(self):
        """Taskni bajarilgan deb belgilash"""
        self.completed = True
        print_satatus(f"'{self.title}' task bajarildi!", 'success')
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        deadline_str = f" (Muddat: {self.deadline})" if self.deadline else ""
        return f"{status} {self.title}{deadline_str}"