from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. URL-ul bazei de date (SQLite creează un fișier numit magazin.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./magazin.db"

# 2. Motorul de conexiune
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necesar doar pentru SQLite
)

# 3. Fabrică de sesiuni (folosită la fiecare request HTTP)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Clasa de bază din care vor moșteni toate tabelele noastre
Base = declarative_base()

# 5. Dependency injection: Deschide o sesiune DB per request și o închide la final
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()