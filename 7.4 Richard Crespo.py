import re

def get_paragraph():
    """
    Prompt the user to enter a paragraph.
    Returns the paragraph as a string.
    """
    paragraph = input("Enter a paragraph: ")
    return paragraph


def extract_sentences(paragraph):
    """
    Extract sentences using a look-ahead regex pattern.

    Updated to support sentences that begin with:
    - A capital letter (A–Z)
    - A digit (0–9)

    Pattern explanation:
    [A-Z0-9]       → Sentence must begin with a capital letter OR a number.
    .*?            → Non-greedy match of any characters.
    [.!?]          → Sentence-ending punctuation.
    (?= [A-Z0-9]|$)
                   → Look-ahead: punctuation must be followed by a space + capital
                     letter/number OR the end of the string.
    """
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)
    return sentences


def display_sentences(sentences):
    """
    Display each sentence and the total number of sentences.
    """
    print("\n--- Individual Sentences ---")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")

    print(f"\nTotal number of sentences: {len(sentences)}")


def main():
    """
    Main program flow:
    1. Get paragraph input
    2. Extract sentences using regex
    3. Display results
    """
    paragraph = get_paragraph()
    sentences = extract_sentences(paragraph)
    display_sentences(sentences)


# Run the program
main()
