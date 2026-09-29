def get_learning_path(topic: str):

    topic = topic.strip()

    if not topic:
        return "Please enter a topic to get learning recommendations."

    return f"""
Learning Path for: {topic}

1. Basic Concepts
- Understand the definition of {topic}
- Learn the basic terms and concepts
- Study simple examples

2. Intermediate Concepts
- Learn how the main concepts work
- Practice with examples
- Solve simple exercises

3. Advanced Concepts
- Study advanced topics related to {topic}
- Work on practical problems
- Build a small project

4. Practice Activities
- Practice regularly
- Solve exercises
- Try practical examples

5. Revision Plan
- Review the basic concepts
- Revise important points
- Practice questions
- Review your mistakes
"""