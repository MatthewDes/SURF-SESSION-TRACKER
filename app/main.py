from fastapi import FastAPI #, HTTPException 
from app.routers import spots, sessions


app = FastAPI() 

app.include_router(spots.router) #I need to learn what this means
app.include_router(sessions.router)
