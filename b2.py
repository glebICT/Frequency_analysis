from collections import Counter
import os

print("🔍 GOLD-BUG CIPHER - Legrand's 6 Steps")
print("=" * 70)

ciphertext = (
    "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;1‡(;:‡*8†83(88)"
    "5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*-4)8¶8*;4069"
    "285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;"
    "48;(88;4(‡?34;48)4‡;161;:188;‡?;"
)

print(f"\n📜 Ciphertext ({len(ciphertext)} chars):")
print(ciphertext)

input("\nPress Enter to begin...")


# ============================================================
# HELPERS
# ============================================================

def decode(text, mapping):
    """Apply current mapping to ciphertext."""
    return ''.join(mapping.get(c, c) for c in text)


def show_step(step, title, explanation, mapping):
    """Display current step neatly."""

    print("\n" + "=" * 70)
    print(f"{step} {title}")
    print(explanation)

    print("\nCurrent mapping:")

    for k, v in sorted(mapping.items()):
        print(f"  {repr(k)} -> {repr(v)}")

    print("\nDecoded text:\n")
    print(decode(ciphertext, mapping))


def extend_mapping(base, additions):
    """
    Safely extend mapping.
    Detects conflicts and duplicate plaintext letters.
    """

    new_mapping = base.copy()

    for cipher_char, plain_char in additions.items():

        # Existing mapping conflict
        if cipher_char in new_mapping:
            old = new_mapping[cipher_char]

            if old != plain_char:
                raise ValueError(
                    f"Conflict: {cipher_char!r} already maps "
                    f"to {old!r}, cannot remap to {plain_char!r}"
                )

        # Duplicate plaintext detection
        for k, v in new_mapping.items():
            if v == plain_char and k != cipher_char:
                print(
                    f"⚠ WARNING: plaintext letter {plain_char!r} "
                    f"already used by {k!r}"
                )

        new_mapping[cipher_char] = plain_char

    return new_mapping


# ============================================================
# FREQUENCY ANALYSIS
# ============================================================

print("\n📊 CHARACTER FREQUENCIES:\n")

freq = Counter(ciphertext)

for char, count in freq.most_common():
    print(f"{repr(char):>4} : {count}")

input("\nPress Enter for STEP 1...")


# ============================================================
# STEP 1 - FREQUENCY ANALYSIS
# ============================================================

mapping = {}

mapping = extend_mapping(mapping, {
    '8': 'e',
    ';': 't',
    '4': 'h',
})

show_step(
    "📊 STEP 1:",
    "FREQUENCY ANALYSIS",
    "\"8\" appears most frequently → probably 'e'",
    mapping
)

input("\nPress Enter...")


# ============================================================
# STEP 2 - DOUBLE LETTERS
# ============================================================

mapping = extend_mapping(mapping, {
    ')': 's',
    '5': 'a',
})

show_step(
    "🔤 STEP 2:",
    "DOUBLE LETTERS / WORD ENDINGS",
    "Patterns like 'ss' and common endings begin appearing",
    mapping
)

input("\nPress Enter...")


# ============================================================
# STEP 3 - COMMON WORDS
# ============================================================

mapping = extend_mapping(mapping, {
    '‡': 'o',
    '3': 'g',
})

show_step(
    "📝 STEP 3:",
    "COMMON WORD PATTERNS",
    "\"good\", \"glass\", and \"hostel\" begin appearing",
    mapping
)

input("\nPress Enter...")


# ============================================================
# STEP 4 - CONTEXTUAL GUESSES
# ============================================================

mapping = extend_mapping(mapping, {
    '*': 'n',
    '6': 'i',
    '(': 'r',
    '†': 'd',
})

show_step(
    "🧩 STEP 4:",
    "SYSTEMATIC EXPANSION",
    "Filling letters using context and English structure",
    mapping
)

input("\nPress Enter...")


# ============================================================
# STEP 5 - COMPLETE MAPPING
# ============================================================

mapping = extend_mapping(mapping, {
    '0': 'l',
    '¶': 'v',
    '1': 'f',
    '2': 'b',
    '9': 'm',
    '?': 'u',
    ':': 'p',
    '-': 'c',
    '.': 'y',
})

show_step(
    "🔓 STEP 5:",
    "FULL SUBSTITUTION KEY",
    "All symbols are now mapped",
    mapping
)

input("\nPress Enter for spacing reconstruction...")


# ============================================================
# STEP 6 - RESTORE SPACES
# ============================================================

print("\n" + "=" * 70)
print("🧠 STEP 6: RESTORING SPACES")
print(
    "The original cipher contains no spaces.\n"
    "Now that the alphabet is solved, words can be separated manually."
)

raw_plaintext = decode(ciphertext, mapping)

print("\nDecoded text without spaces:\n")
print(raw_plaintext)

input("\nPress Enter to reconstruct spacing...")


# Reconstructed message
final_plaintext = (
    "a good glass in the bishop's hostel in the devil's seat "
    "forty-one degrees and thirteen minutes northeast and by north "
    "main branch seventh limb east side shoot from the left eye "
    "of the death's-head a bee-line from the tree through the shot "
    "fifty feet out"
)

print("\n" + "=" * 70)
print("🎉 FINAL TREASURE DIRECTIONS:\n")

print(final_plaintext)

print("\n" + "=" * 70)
print("📚 Explanation:")
print(
    "Poe removed spaces and punctuation to make frequency\n"
    "analysis harder. Once the substitution alphabet is solved,\n"
    "the cryptanalyst must still reconstruct word boundaries."
)


# ============================================================
# SAVE OUTPUT
# ============================================================

os.makedirs("output", exist_ok=True)

with open("output/goldbug_5steps.txt", "w", encoding="utf-8") as f:
    f.write(final_plaintext)

print("\n💾 Saved to output/goldbug_5steps.txt")