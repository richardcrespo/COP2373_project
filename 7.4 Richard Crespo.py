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
    Extract sentences using the Section 7.4 look-ahead regex pattern.

    Pattern explanation:
    [A-Z]          → A sentence must begin with a capital letter.
    .*?            → Non-greedy match of any characters.
    [.!?]          → Sentence-ending punctuation.
    (?= [A-Z]|$)   → Look-ahead: punctuation must be followed by a space + capital letter
                     OR the end of the string. This prevents consuming characters like
                     abbreviations (U.S.A.) or decimals (65.5).
    """
    pattern = r'[A-Z].*?[.!?](?= [A-Z]|$)'

    # DOTALL allows '.' to match newlines
    # MULTILINE allows look-ahead to match end-of-line as end-of-string
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
