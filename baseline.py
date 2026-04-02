from resume_env import ResumeEnv

def run_baseline():
    env = ResumeEnv()

    tasks = ["easy", "medium", "hard"]
    results = {}

    for task in tasks:
        state = env.reset(task)

        resumes = state["data"]["resumes"]

        # simple logic: pick candidate with highest experience
        best_candidate = max(resumes, key=lambda x: x["experience"])["name"]

        _, reward, _, _ = env.step({"selected_candidate": best_candidate})

        results[task] = reward

    return results


if __name__ == "__main__":
    scores = run_baseline()
    print("Baseline Scores:", scores)