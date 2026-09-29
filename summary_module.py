def summarize_text(text: str) -> str:

    text = text.strip()

    if not text:
        return "Please enter a paragraph to summarize."

    # Split paragraph into sentences
    sentences = [
        sentence.strip()
        for sentence in text.replace("\n", " ").split(".")
        if sentence.strip()
    ]

    if not sentences:
        return "Unable to create a summary."

    # Take up to 2 complete sentences
    summary_sentences = sentences[:2]

    return "\n\n".join(
        f"• {sentence}."
        for sentence in summary_sentences
    )