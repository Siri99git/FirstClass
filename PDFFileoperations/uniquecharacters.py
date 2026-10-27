words = ["apple", "banana", "cherry"]
seen_chars = set()
total_chars = 0

for word in words:
  for char in word:
    seen_chars.add(char)  # Hashset stores unique characters
    total_chars += 1  # Total character count

print("Total characters:", total_chars)
print("Unique characters hashset:", seen_chars)
