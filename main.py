from fastapi import FastAPI

from routers import test

app = FastAPI(
    title='Magic Pinecone Backend API',
    description='A project allows NCUers to retrieval the massive campus information in this single platform.',
    version='0.0.0',
    contact={
        'name': 'Shawn Lin',
        'email': 'spig100.roc@gmail.com'
    }
)

app.include_router(test.router)

@app.get("/")
def root():
    return {"message": "Welcome to Amazing Pinecone Backend!"}