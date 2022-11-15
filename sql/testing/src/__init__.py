from core.database import create_connection

if __name__ == "__main__":
    db = create_connection()

    db.close()