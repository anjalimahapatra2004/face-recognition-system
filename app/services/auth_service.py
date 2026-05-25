import uuid

class AuthService:

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())