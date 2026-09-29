def explain_topic(topic: str) -> str:

    topic = topic.strip()

    # Offline fallback explanation
    if topic.lower() == "recursion":
        return """
1. Simple Definition:
Recursion is a programming technique where a function calls itself to solve a problem.

2. How it works:
A recursive function solves a smaller version of the same problem again and again.
It must have a base condition to stop the function from calling itself forever.

3. Easy Example:
Finding the factorial of a number is a common example.
For example, 3! = 3 × 2 × 1 = 6.
"""

    if topic.lower() in ["artificial intelligence", "ai"]:
        return """
1. Simple Definition:
Artificial Intelligence (AI) is technology that enables computers to perform tasks that normally require human intelligence.

2. How it works:
AI systems learn from data, identify patterns, and use those patterns to make predictions or decisions.

3. Easy Example:
A voice assistant that understands a user's spoken question and provides an answer is an example of AI.
"""

    if topic.lower() == "python":
        return """
1. Simple Definition:
Python is a high-level programming language known for its simple and readable syntax.

2. How it works:
Python programs are written as instructions that are executed by the Python interpreter.

3. Easy Example:
Python can be used to calculate numbers, process data, build websites, and create AI applications.
"""

    # Generic fallback
    return f"""
1. Simple Definition:
{topic} is an important concept that can be understood by learning its basic ideas and purpose.

2. How it works:
The concept of {topic} can be understood by studying its main components and how they work together.

3. Easy Example:
A simple example or practical application of {topic} can help a student understand the concept better.
"""