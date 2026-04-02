from fastapi import FastAPI
from resume_env import ResumeEnv
from grader import grade
from baseline import run_baseline

# ------------------ INIT ------------------
app = FastAPI()
env = ResumeEnv()

# ------------------ ROOT ------------------
@app.get("/")
def home():
    return {"message": "Resume Environment Running"}

# ------------------ RESET ------------------
@app.get("/reset")
def reset(task: str = "easy"):
    return env.reset(task)

# ------------------ STEP ------------------
@app.post("/step")
def step(action: dict):
    return env.step(action)

# ------------------ STATE ------------------
@app.get("/state")
def state():
    return env.state()

# ------------------ TASKS ------------------
@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            {
                "name": "easy",
                "description": "Select candidate with Python skill"
            },
            {
                "name": "medium",
                "description": "Select candidate with Python + ML + 2 years experience"
            },
            {
                "name": "hard",
                "description": "Select best candidate for Senior ML Engineer"
            }
        ],
        "action_format": {
            "selected_candidate": "string"
        }
    }

# ------------------ GRADER ------------------
@app.post("/grader")
def grader_api(task: str, selected_candidate: str):
    score = grade(task, selected_candidate)
    return {
        "task": task,
        "selected_candidate": selected_candidate,
        "score": score
    }

# ------------------ BASELINE ------------------
@app.get("/baseline")
def baseline():
    scores = run_baseline()
    return {
        "baseline_scores": scores
    }