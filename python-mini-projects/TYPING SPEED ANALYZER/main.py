import time

# Sample text for typing test
test_text = (
    "Python is a powerful and easy to learn programming language "
    "used for web development data science artificial intelligence "
    "and automation."
)

print("===== Typing Speed Analyzer =====")
print("\nType the following text:\n")
print(test_text)
print("\nPress ENTER when you are ready...")
input()

start_time = time.time()

typed_text = input("\nStart typing here:\n")

end_time = time.time()

# Time calculation
time_taken = end_time - start_time
time_minutes = time_taken / 60

# Word count
typed_words = typed_text.split()
word_count = len(typed_words)

# WPM calculation
wpm = word_count / time_minutes if time_minutes > 0 else 0

# Accuracy calculation
correct_chars = 0
for i in range(min(len(test_text), len(typed_text))):
    if test_text[i] == typed_text[i]:
        correct_chars += 1

accuracy = (correct_chars / len(test_text)) * 100

# Results
print("\n===== Results =====")
print(f"Time Taken: {round(time_taken, 2)} seconds")
print(f"Words Per Minute (WPM): {round(wpm, 2)}")
print(f"Accuracy: {round(accuracy, 2)}%")

# Performance Feedback
if wpm >= 60:
    print("Typing Level: Excellent 🚀")
elif wpm >= 40:
    print("Typing Level: Good 👍")
elif wpm >= 25:
    print("Typing Level: Average 🙂")
else:
    print("Typing Level: Needs Practice ⚠️")
