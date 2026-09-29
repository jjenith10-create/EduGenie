def generate_quiz(topic: str):

    topic = topic.lower().strip()

    # Computer Basics fallback quiz
    if "computer" in topic or "computer basics" in topic:
        return {
            "quiz": [
                {
                    "question": "What does CPU stand for?",
                    "options": [
                        "Central Processing Unit",
                        "Computer Personal Unit",
                        "Central Peripheral Unit",
                        "Control Power Unit"
                    ],
                    "answer": "Central Processing Unit"
                },
                {
                    "question": "Which of the following is volatile memory?",
                    "options": [
                        "HDD",
                        "ROM",
                        "RAM",
                        "SSD"
                    ],
                    "answer": "RAM"
                },
                {
                    "question": "Which of the following is an input device?",
                    "options": [
                        "Monitor",
                        "Keyboard",
                        "Speaker",
                        "Printer"
                    ],
                    "answer": "Keyboard"
                }
            ]
        }

    # General fallback quiz
    return {
        "quiz": [
            {
                "question": f"What is an important first step when learning {topic}?",
                "options": [
                    "Understand the basic concepts",
                    "Skip all basics",
                    "Avoid practice",
                    "Stop after one lesson"
                ],
                "answer": "Understand the basic concepts"
            },
            {
                "question": f"Which activity is useful for learning {topic}?",
                "options": [
                    "Regular practice",
                    "Never reviewing",
                    "Ignoring examples",
                    "Avoiding exercises"
                ],
                "answer": "Regular practice"
            },
            {
                "question": f"How can a student improve knowledge of {topic}?",
                "options": [
                    "Practice and revision",
                    "Only guessing",
                    "Never studying",
                    "Skipping important concepts"
                ],
                "answer": "Practice and revision"
            }
        ]
    }