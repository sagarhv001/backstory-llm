from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load your fine-tuned model
tokenizer = AutoTokenizer.from_pretrained("backstory")
model = AutoModelForCausalLM.from_pretrained("backstory")

@app.get("/", response_class=HTMLResponse)
async def chat_ui(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/api/generate")
async def generate_text(
    name: str = Form(...),
    description: str = Form(...)
):
    prompt = (
        f"Write a vivid, emotionally grounded backstory for the following character. Avoid meta-commentary, real-world references, or speculation. based on the following:\n"
        f"Name: {name}\n"
        f"Description: {description}\n"
        f"Backstory:"
    )


    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=512,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        repetition_penalty=1.5,
        pad_token_id=tokenizer.eos_token_id
    )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract the backstory field from output
    if "Backstory:" in result:
        backstory = result.split("Backstory:")[1].strip()
    else:
        backstory = result.strip()


    return JSONResponse({
        "name": name,
        "description": description,
        "backstory": backstory
    })

@app.get("/generate")
async def generate_via_get(name: str = Query(...), description: str = Query(...)):
    prompt = (
    f"Write a vivid, emotionally grounded backstory for the following character. Avoid meta-commentary, real-world references, or speculation.\n"
    f"Name: {name}\n"
    f"Description: {description}\n"
    f"Backstory:"   
    )



    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=512,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        repetition_penalty=1.5,
        pad_token_id=tokenizer.eos_token_id
    )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if "Backstory:" in result:
        backstory = result.split("Backstory:")[1].strip()
    else:
        backstory = result.strip()
    return JSONResponse({
        "name": name,
        "description": description,
        "backstory": backstory
    })

@app.get("/status")
async def get_status():
    return {
        "status": "online",
        "model": "backstory",
        "time": datetime.now().isoformat(),
        "device": str(torch.device("cuda" if torch.cuda.is_available() else "cpu"))
    }
