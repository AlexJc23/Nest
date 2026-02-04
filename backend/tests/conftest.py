# tests/conftest.py
import sys
from pathlib import Path

# --- path setup MUST come first ---
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

# --- now imports work ---
import pytest
from app.schemas.users import UserResponse

@pytest.fixture
def fake_user():
    return UserResponse(
        id=99,
        email="test@example.com",
        first_name="Test",
        last_name="User",
        role="admin",
        is_active=True,
        branch_id=99,
    )
