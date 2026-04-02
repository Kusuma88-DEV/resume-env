# class ResumeEnv:
#     def __init__(self):
#         self.state_data = None

#     def reset(self):
#         self.state_data = {
#             "resumes": [
#                 {"name": "Alice", "skills": ["python", "ml"], "experience": 2},
#                 {"name": "Bob", "skills": ["java"], "experience": 1}
#             ],
#             "job_role": "ML Engineer"
#         }
#         return self.state_data

#     def step(self, action):
#         selected = action.get("selected_candidate")

#         correct = "Alice"

#         if selected == correct:
#             reward = 1.0
#             done = True
#         else:
#             reward = 0.0
#             done = True

#         return self.state_data, reward, done, {}

#     def state(self):
#         return self.state_data
# class ResumeEnv:
#     def __init__(self):
#         self.state_data = None
#         self.current_task = None

#     def reset(self, task="easy"):
#         self.current_task = task

#         if task == "easy":
#             self.state_data = {
#                 "resumes": [
#                     {"name": "Alice", "skills": ["python"], "experience": 1},
#                     {"name": "Bob", "skills": ["java"], "experience": 1}
#                 ],
#                 "job_role": "Python Developer"
#             }

#         elif task == "medium":
#             self.state_data = {
#                 "resumes": [
#                     {"name": "Alice", "skills": ["python", "ml"], "experience": 2},
#                     {"name": "Bob", "skills": ["python"], "experience": 1}
#                 ],
#                 "job_role": "ML Engineer"
#             }

#         elif task == "hard":
#             self.state_data = {
#                 "resumes": [
#                     {"name": "Alice", "skills": ["python", "ml"], "experience": 2},
#                     {"name": "Bob", "skills": ["python", "ml"], "experience": 3}
#                 ],
#                 "job_role": "Senior ML Engineer"
#             }

#         return {"task": task, "data": self.state_data}

    # def step(self, action):
    #     selected = action.get("selected_candidate")

    #     correct = self.get_correct_answer()

    #     if selected == correct:
    #         reward = 1.0
    #     elif selected is not None:
    #         reward = 0.5
    #     else:
    #         reward = 0.0

    #     done = True

    #     return self.state_data, reward, done, {}
    # from grader import grade   # ADD THIS AT TOP

    # def step(self, action):
    #         selected = action.get("selected_candidate")

    #          reward = grade(self.current_task, selected)

    #         done = True

    #         return self.state_data, reward, done, {} 

    # def get_correct_answer(self):
    #     if self.current_task == "easy":
    #         return "Alice"
    #     elif self.current_task == "medium":
    #         return "Alice"
    #     elif self.current_task == "hard":
    #         return "Bob"

    # def state(self):
    #     return self.state_data
from grader import grade   # ✅ MUST be at top

class ResumeEnv:
    def __init__(self):
        self.state_data = None
        self.current_task = None

    def reset(self, task="easy"):
        self.current_task = task

        if task == "easy":
            self.state_data = {
                "resumes": [
                    {"name": "Alice", "skills": ["python"], "experience": 1},
                    {"name": "Bob", "skills": ["java"], "experience": 1}
                ],
                "job_role": "Python Developer"
            }

        elif task == "medium":
            self.state_data = {
                "resumes": [
                    {"name": "Alice", "skills": ["python", "ml"], "experience": 2},
                    {"name": "Bob", "skills": ["python"], "experience": 1}
                ],
                "job_role": "ML Engineer"
            }

        elif task == "hard":
            self.state_data = {
                "resumes": [
                    {"name": "Alice", "skills": ["python", "ml"], "experience": 2},
                    {"name": "Bob", "skills": ["python", "ml"], "experience": 3}
                ],
                "job_role": "Senior ML Engineer"
            }

        return {"task": task, "data": self.state_data}

    def step(self, action):
        selected = action.get("selected_candidate")

        reward = grade(self.current_task, selected)

        done = True

        return self.state_data, reward, done, {}

    def state(self):
        return self.state_data