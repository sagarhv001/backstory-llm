# Backstory Generator
Backstory Generator is a microservice that generates immersive, lore-rich character backstories using a fine‑tuned language model.
The model was fine‑tuned in an unsupervised manner using narrative text from the public dataset baebee/Little-Literature. 
The project exposes a FastAPI interface (with a web UI and API endpoints) so that prompts can be submitted and backstories are returned.

# Table of Contents

- [What It Does](#what-it-does)
- [File Structure](#file-structure)
- [How to Run](#how-to-run)
- [Dataset Source & Processing](#dataset-source--processing)
- [Sample Input/Output](#sample-inputoutput)
- [Requirements](#requirements)
- [What I’d Improve With More Time](#What-I'-d-Improve-With-More-Time)
- [Screenshots](#Screenshots)

# What It Does
Generates Narrative Backstories:
The service uses a fine‑tuned DistilGPT‑2 model (named “backstory”) that has learned from a curated corpus of narrative texts. It produces coherent and lore‑rich backstories for game characters.

API & UI Interface:

API Endpoints:

POST /api/generate: Accepts character name and description, then returns a generated backstory.

GET /generate: Alternative endpoint to allow testing via URL query parameters.

GET /status: Returns API status, model name, timestamp, and device (CPU/GPU) info.

Interactive UI:
A simple web UI (using Jinja2 templates with HTML/JS) that allows users to enter a character’s name and description and receive the generated backstory in a typewriter animation style.

Unsupervised Fine-Tuning:
Instead of training on explicit prompt–completion pairs, the model was trained on a large corpus of narrative texts (from baebee/Little-Literature), learning to continue text in a lore-rich style.

# File Structure

                  backstory-llm/
                  ├── app.py                   # FastAPI application exposing /generate and /status endpoints
                  ├── templates/               
                  │   └── form.html            # HTML/Jinja2 template for the web UI
                  ├── static/                  
                  │   └── styles.css           # CSS file for UI styling
                  |   └── chat.js 
                  ├── backstory/               # Directory containing the fine-tuned model files        
                  │   └── added_tokens.json 
                  │   └── config.json
                  │   └── generation_config.json
                  │   └── merges.txt
                  │   └── model.safetensors
                  │   └── special_tokens_map.json
                  │   └── tokenizer.json
                  │   └── tokenizer_config.json
                  │   └── training_args.bin
                  │   └── vocab.json
                  ├── game-backstory.ipynb/    # Notebook for data preprocessing and fine-tuning           
                  ├── requirements.txt         # Python dependency file (see below)
                  └── README.md                # This README file

# How to Run
## Local Setup
Clone the Repository

bash

                  git clone https://github.com/sagarhv001/backstory-llm.git
                  cd backstory-generator
Install Dependencies

Install the necessary packages by running:

bash

                  pip install -r requirements.txt
(See the Requirements section below for details.)

Run the API

Launch the API with Uvicorn:

bash
      
                  uvicorn app1:app --reload
                  
The server will run at http://localhost:8000.

Access the UI

Open your browser and navigate to http://localhost:8000 to use the interactive web form to generate backstories.

Test API Endpoints

Generate Backstory (POST):

bash

                  curl -X POST http://localhost:8000/api/generate \
                  -H "Content-Type: application/x-www-form-urlencoded" \
                  -d "name=Kaylon&description=An empire of androids that killed their biological creators."
API Status:

bash

                  curl http://localhost:8000/status

# Dataset Source & Processing
## Source:
The model was fine‑tuned using the dataset baebee/Little-Literature available on Hugging Face.

## Processing:
The raw text was cleaned and divided into blocks, then used for unsupervised fine‑tuning. Data processing details (tokenization, grouping into fixed‑length sequences) are documented in the training notebook.

## Sample Input/Output
Example API Input
Name: Kaylon
Description: An empire of androids that killed their biological creators.

                  output:The universe is now dominated with tales woven from time to moment in space's endless history books through stories that trace themselves into life itself  It was this journey we began                   - as it stood tall against its cosmic weighting force at every step until they reached stride beyond reach...
                  As one day passedby I felt lost forever within my grasp just beneath meadows like graceful grooves across infinity all over each bendI gazed uponThe Last Leaf And watched
                  A shimmered gleam amidst eternal nightfallAnd dancedWith longingFor breathless peaceand blissfor beautyInvisible lightnessOf darknessTo dancewith joyof harmony
                  That would flowThrough vast open roadBut withered tongueWhispers entwinedWhen whispers spreadAcross infinite horizonThorn songbearerWho wanedSo kissedWhere sorrow came'On thorns sang
                  Now whisperThough weary Here dartedLongest sewedEart treadsUpon flowerbreakTwistedThen roseBeheldHere glisteningAlong leafdriedThere shall be no end but despairOne love foundsturned
                  All seek refugeDeep seaBeyond midnightTreadied there may come', But what remains liesWhat remain stands undiscoveredDiluted deep below your heartOath shoreboundBreathneath sky above you                         gentle breeze
                  Let go softlyCome gentlyMay take comfortFrom pain so dearWoven never let fallThis land awaits yetYet silenceSept unseenIs here residesLiving still
                  It sings 'a tale toldin existence form"Song sung singalongCrying soft touch between thoughtsWhich brings laughter

# Requirements
The project relies on the following Python packages:


      fastapi
      uvicorn
      transformers
      torch
      jinja2
      python-multipart
      datasets
      accelerate
      aiofiles
      nest_asyncio
# What I’d Improve With More Time
Data Quality and Volume:
Further curate and expand the dataset with additional lore from gaming universes for richer, more context-aware generation.

Model Enhancement:
Experiment with larger models or efficient fine‑tuning techniques like LoRA to improve generation quality without a huge resource penalty.

Prompt Engineering:
Refine prompts with few-shot examples to better control the style and coherence of generated backstories.

Front-end and UX:
Enhance the UI with interactive elements, multi-turn conversations, and modern styling (e.g., a chat-like interface similar to ChatGPT).

Deployment and Scaling:
Containerize the application using Docker and set up CI/CD pipelines for seamless deployment, plus integrate analytics and logging for production monitoring.

Additional API Features:
Add endpoints for logging requests, error handling, and possibly a dashboard for model metrics.
# Screenshots


