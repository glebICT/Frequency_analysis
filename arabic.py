ALPHABET = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"
frequency_order = "ايلمونرهتسكدعفبجحقهويطشصضغثخذزظ"

def generate_caesar_key(offset: int) -> dict[str, str]:
    offset = offset % 26
    return {
        ch: ALPHABET[(i + offset) % 26]
        for i, ch in enumerate(ALPHABET)
    }

def switch_encode(text: str, key: dict[str, str]) -> str:
    return ''.join(
        key.get(ch.lower(), ch)   # keep spaces, punctuation as is
        for ch in text
    )

def switch_decode(text: str, key: dict[str, str]) -> str:
    inverse = {v: k for k, v in key.items()}
    return ''.join(
        inverse.get(ch.lower(), ch)
        for ch in text
    )

key = generate_caesar_key(3)  
print(key)
encoded = switch_encode('مرحبا بالعالم!', key)
print(encoded)

decoded = switch_decode(encoded, key)
print(decoded)
