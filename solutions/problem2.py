def solve_problem2():
    with open("inputs/problem2_input.txt") as f:
        s = f.read().strip()

    # 1. Reverse
    s = s[::-1]

    # 2. Remove every 3rd character
    s = ''.join(ch for i, ch in enumerate(s) if (i + 1) % 3 != 0)

    # 3. Shift ASCII +2
    shifted = ''.join(chr(ord(ch) + 2) for ch in s)

    # 4. Count vowels
    vowels = "aeiouAEIOU"
    vowel_count = sum(ch in vowels for ch in shifted)

    print(vowel_count)
    return vowel_count

if __name__ == "_main_":
    solve_problem2()