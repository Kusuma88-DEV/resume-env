def grade(task, selected_candidate):
    
    # correct answers
    correct_answers = {
        "easy": "Alice",
        "medium": "Alice",
        "hard": "Bob"
    }

    correct = correct_answers.get(task)

    if selected_candidate == correct:
        return 1.0
    elif selected_candidate is not None:
        return 0.5
    else:
        return 0.0