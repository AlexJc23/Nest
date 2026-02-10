from datetime import datetime

class UserModel:
    def __init__(self, id: int, hashed_password: str, email: str, first_name: str, last_name: str, role: str, is_active: bool, title: str = None, driving_score: int = None, nps_score: int = None, branch_id: int = 0, profile_img_url: str = None, google_chat_email: str = None, created_at=datetime.utcnow(), updated_at=datetime.utcnow()):
        self.id = id
        self.hashed_password = hashed_password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.is_active = is_active
        self.title = title
        self.driving_score = driving_score
        self.nps_score = nps_score
        self.branch_id = branch_id
        self.profile_img_url = profile_img_url
        self.google_chat_email = google_chat_email
        self.created_at = created_at
        self.updated_at = updated_at
