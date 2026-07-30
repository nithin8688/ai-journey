from fastapi import FastAPI, HTTPException, Depends, Request 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from typing import List 
import os 
import json 

# Importing my modules 
from file_organize import FileOrganizer 
from auth import Token, get_current_user, verify_password, create_access_token, fake_users_db 

app = FastAPI(
    title="File Organizer API",
    description="organize your files via API endpoints",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OrganizeRequest(BaseModel):
    source_folder: str 

class PlannedMove(BaseModel):
    file: str 
    from_path: str = Field(alias="from")
    to_path: str = Field(alias="to")
    category: str 

    class Config:
        populate_by_name = True 

class MoveLog(BaseModel):
    filename: str
    destination: str 
    action: str 
    timestamp: str

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )

    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )
    token = create_access_token(data={"sub":form_data.username})
    return {"access_token": token, "token_type":"bearer"}

@app.post("/organize/dry-run", response_model=List[PlannedMove])
async def dry_run(request: OrganizeRequest):
    if not os.path.exists(request.source_folder):
        raise HTTPException(status_code=404, detail="Folder not found")
    org = FileOrganizer(request.source_folder)
    planned_moves = org.dry_run()
    return planned_moves

@app.post("/organize/run")
async def run(request: OrganizeRequest, current_user: str = Depends(get_current_user)):
    if not os.path.exists(request.source_folder):
        raise HTTPException(status_code=404, detail="File not found")
    org = FileOrganizer(request.source_folder)
    move_log = org.organize() 
    return {
        "message": f"Organized by {current_user['username']}",
        "total_moved": len(move_log),
        "move_log": move_log
    }

@app.get("/organize/log")
async def get_log(source_folder: str, current_user = Depends(get_current_user)):
    log_path = os.path.join(source_folder, "move_log.json")

    if not os.path.exists(log_path):
        raise HTTPException(
            status_code=404,
            detail="Log file not found"
        )
    with open(log_path,"r") as f:
        contents = json.load(f)
    return contents