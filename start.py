import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.core.app:app", port=8080, host="127.0.0.1", reload=True)
