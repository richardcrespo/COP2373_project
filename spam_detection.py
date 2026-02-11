# ---------------------------------------------
# Spam Detection Program By Richard Crespo
# ---------------------------------------------
# This program scans a user-provided email message
# for 30 common spam keywords/phrases. Each match
# increases the spam score by 1. The program then
# displays the score, the likelihood of spam, and
# which words triggered the score.
# ---------------------------------------------

# Function: returns a list of 30 spam keywords/phrases
def get_spam_keywords():
    return [
        "free", "winner", "cash prize", "congratulations", "act now",
        "limited time", "urgent", "risk-free", "100% guaranteed",
        "click here", "call now", "exclusive deal", "offer expires",
        "cheap", "lowest price", "earn money", "work from home",
        "investment", "credit card", "debt relief", "pre-approved",
        "no obligation", "apply now", "bonus", "double your income",
        "miracle", "weight loss", "viagra", "free trial",
        "money-back guarantee"
    ]

# Function: evaluates spam score and returns likelihood label
def rate_spam(score):
    if score == 0:
        return "Very unlikely to be spam"
    elif score <= 3:
        return "Possibly spam"
    elif score <= 7:
        return "Likely spam"
    else:
        return "Highly likely spam"

# ---------------------------------------------
# Main Program
# ---------------------------------------------
def main():
    print("=== Spam Detection Tool ===")
    message = input("Enter the email message to analyze:\n").lower()

    keywords = get_spam_keywords()
    spam_score = 0
    triggered_words = []

    # Scan message for each keyword
    for word in keywords:
        if word in message:
            spam_score += 1
            triggered_words.append(word)

    # Determine likelihood
    likelihood = rate_spam(spam_score)

    # Display results
    print("\n=== Spam Analysis Results ===")
    print(f"Spam Score: {spam_score}")
    print(f"Likelihood: {likelihood}")

    if triggered_words:
        print("\nKeywords detected:")
        for w in triggered_words:
            print(f" - {w}")
    else:
        print("\nNo spam keywords detected.")

# Run the program
if __name__ == "__main__":
    main()
