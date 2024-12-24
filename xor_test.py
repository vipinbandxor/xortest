def count_repeat_spell(letters: str, target: str) -> int:
    # Count frequency of each character in target word and input letters
    target_freq = [target.count(char) for char in set(target)]
    input_freq = [letters.upper().count(char) for char in set(target)]

    # return int value, how many times the word can be formed
    return min(input_freq[i] // target_freq[i] for i in range(len(target_freq)))


bowl_of_letters = "PENNYMACPENNYMCTRUEIWPENNYMCAAAA"
target = "PENNYMAC"
result = count_repeat_spell(bowl_of_letters,target)
print(f"{target} can be spelled: {result} times")
