from app import app

if __name__ == "__main__":
    from uvicorn import run
    run(
        "app:app",
        host="localhost",
        port=8000,
        reload=True
    )