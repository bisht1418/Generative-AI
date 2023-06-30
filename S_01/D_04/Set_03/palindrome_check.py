def is_palindrome(word):
    word = word.lower()  # Convert the word to lowercase
    reversed_word = word[::-1]  # Reverse the word

    if word == reversed_word:
        return f"The word {word} is a palindrome."
    else:
        return f"The word {word} is not a palindrome."


# Example usage:
input_word = "madam"
result = is_palindrome(input_word)
print(result)

# ================================================================


# def is_palindrome(word):
#     word = word.lower()  # Convert the word to lowercase
#     length = len(word)

#     for i in range(length // 2):
#         if word[i] != word[length - i - 1]:
#             return f"The word {word} is not a palindrome."

#     return f"The word {word} is a palindrome."


# # Example usage:
# input_word = "madam"
# result = is_palindrome(input_word)
# print(result)
