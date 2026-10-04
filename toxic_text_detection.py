import re

print("=" * 60)
print("             TOXIC TEXT DETECTION")
print("=" * 60)

toxic_words = [
    "hate",
    "stupid",
    "idiot",
    "fool",
    "loser",
    "shut up",
    "useless",
    "moron",
    "nonsense",
    "disgusting"
]

def detect_toxicity(text):
    text = text.lower()
    score = 0

    for word in toxic_words:
        if re.search(r"\b" + re.escape(word) + r"\b", text):
            score += 1

    if score >= 1:
        return "TOXIC"
    else:
        return "NON-TOXIC"


text = input("\nEnter a message:\n")

result = detect_toxicity(text)

print("\nText:", text)
print("Classification:", result)