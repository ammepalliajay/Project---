"""
Project Data Models Module
Defines all data structures and models.
"""

class ProjectModel:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.created_at = None
    
    def to_dict(self):
        """Convert model to dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at
        }
