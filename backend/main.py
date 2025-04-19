import os
from dotenv import load_dotenv
from typing import Union
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

@app.get("/")
async def landing_page():
    greet = {
        "message" : "Welcome to the world of Solo-Leveling System!" ,
        "message2" : "Me, The System Welcomes you!"
    }
    return greet 

@app.get("/greeting/{name}")
async def greet_user(name : str , rank : Union[str , None] = None):
    print("Name", name)
    greetings = f"""Hi , How are you {name}! Have you been recently awakened. Welcome to the system, Best of luck on your solo levelin journey. I see your rank is {rank}
              """
    return  {"greeting" : greetings}    