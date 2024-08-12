import difflib

text1 = "Hello, world!"
text2 = "Hello, Python world!"

diff = difflib.ndiff(text1, text2)
print(''.join(diff))
# H  e  l  l  o  ,   + P+ y+ t+ h+ o+ n+    w  o  r  l  d  !

# SequenceMatcher를 사용한 유사도 비율 계산
similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
print(f"Similarity: {similarity:.2f}")  # Similarity: 0.84

# word close match
words = ["apple", "orange", "banana", "grape", "pineapple"]
target = "appel"

# similarity word search
close_matches = difflib.get_close_matches(target, words)
print(f"Close matches for '{target}': {close_matches}")
# Close matches for 'appel': ['apple', 'pineapple']

# Sentence lists and sentences to compare
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A slow white dog runs the cat.",
    "The quick red fox jumps over the sleepy cat."
]
target_sentence = "The quick brown fox jumps over a lazy dog."

close_matches = difflib.get_close_matches(target_sentence, sentences)
print(f"Close matches for '{target_sentence}': {close_matches}")
# Close matches for 'The quick brown fox jumps over a lazy dog.':
# ['The quick brown fox jumps over the lazy dog.',
# 'The quick red fox jumps over the sleepy cat.']

# file to list
with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()

# HtmlDiff use list diff
diff = difflib.HtmlDiff().make_file(file1_lines, file2_lines,
                                    fromdesc='File 1', todesc='File 2')

# Save result
with open('diff.html', 'w') as result_file:
    result_file.write(diff)
