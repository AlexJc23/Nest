from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection string
# sqlite:/// = use SQLite
# ./app.db = database file in the current project directory
DATABASE_URL = "sqlite:///./app.db"

# Create the SQLAlchemy engine
# The engine is the LOW-LEVEL connection manager to the database
# It knows how to talk to SQLite, but it does NOT manage sessions or transactions
#
# check_same_thread=False is REQUIRED for SQLite when used with FastAPI
# because FastAPI handles requests across multiple threads
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session factory
# This does NOT open a DB connection yet
# It creates a CLASS that can later create sessions
#
# autocommit=False → you must explicitly commit changes
# autoflush=False → SQLAlchemy won’t auto-sync changes until you ask
# bind=engine → sessions created here will use the engine above
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependency function for FastAPI
# This is how each request safely gets its own DB session
def get_db():
    # Create a new database session
    # This is a UNIT OF WORK for a single request
    db = SessionLocal()
    try:
        # Yield hands the session to the path operation (endpoint)
        # FastAPI pauses here, runs the request, then resumes after
        yield db
    finally:
        # This ALWAYS runs, even if an exception occurs
        # Prevents connection leaks and locked SQLite files
        db.close()
