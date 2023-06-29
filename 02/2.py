# 4. Replace Multiple Spaces with a Single Space
# sentence = "This   is a    sample   sentence with spaces."

# your code here

# result = "This is a sample sentence with spaces."

sentence = "This   is a    sample   sentence with spaces."
print(sentence.split())
print(' '.join(sentence.split()))
