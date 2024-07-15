import requests
from datetime import datetime, timedelta

class InstanceAPI:
    def __init__(self, api_url, email, password):
        """Initialize the API client."""
        self.api_url = api_url
        self.email = email
        self.password = password
        self.token = None
        self.token_expiration = None

    def authenticate(self):
        """Authenticate and get a new token."""
        auth_url = f"{self.api_url}/auth"
        data = {"email": self.email, "password": self.password}
        response = requests.post(auth_url, json=data)
        if response.status_code == 200:
            result = response.json()
            if result['success'] == 'true':
                self.token = result['token']
                self.token_expiration = datetime.now() + timedelta(hours=24)
                return True
        return False

    def ensure_token_valid(self):
        """Ensure the token is valid, renewing if necessary."""
        if self.token is None or self.token_expiration is None or datetime.now() >= self.token_expiration:
            return self.authenticate()
        return True

    def get_instance_info(self):
        """Get instance information."""
        if not self.ensure_token_valid():
            return None
        
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.api_url}/instance", headers=headers)
        if response.status_code == 200:
            return response.json()
        return None

    def start_instance(self):
        """Start the instance."""
        if not self.ensure_token_valid():
            return False
        
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(f"{self.api_url}/instance/start", headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result['success'] == 'true'
        return False

    def stop_instance(self):
        """Stop the instance."""
        if not self.ensure_token_valid():
            return False
        
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(f"{self.api_url}/instance/stop", headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result['success'] == 'true'
        return False