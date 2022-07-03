from string import ascii_lowercase as alphabet


def cesar(msg: str, turns: int, encode: bool) -> str:
    encrypted_word = ""
    encrypted_words = []

    words_to_be_encrypted = msg.split()
    for word in words_to_be_encrypted:
        for letter in word:
            if encode:
                new_index = alphabet.find(letter) + turns
                new_letter = alphabet[new_index if new_index <= 26 else new_index - 26]
            else:
                new_index = alphabet.find(letter) - turns
                new_letter = alphabet[new_index if new_index <= 26 else new_index + 26]

            encrypted_word += new_letter

        encrypted_words.append(encrypted_word)
        encrypted_word = ""

    encrypted_msg = " ".join(encrypted_words)

    return encrypted_msg
