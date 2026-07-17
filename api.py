"""
Project API Module
Defines all API endpoints and handlers.
"""

class APIHandler:
    def __init__(self):
        self.endpoints = {}
    
    def register_endpoint(self, path, method):
        """Register a new API endpoint."""
        self.endpoints[path] = method
    
    def handle_request(self, path):
        """Handle incoming API request."""
        if path in self.endpoints:
            return self.endpoints[path]()
