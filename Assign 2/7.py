# Function to count characters in a sentence
def key_value(sentence):
    counts = {}
    for char in sentence:
        if char != " ":  # Ignore spaces
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

# Example usage
text = "The British College"
result = key_value(text)
print(result)