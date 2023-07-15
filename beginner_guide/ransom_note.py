def canConstruct(ransomNote: str, magazine: str) -> bool:
    """ return true if ransomNote can be constructed by using 
    the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.
    """

    # Create a dictionary to store the frequency of each character in magazine
    magazine_dict = {}

    for char in magazine:
        if char in magazine_dict:
            magazine_dict[char] += 1
        else:
            magazine_dict[char] = 1

    # Loop through each character in ransomNote
    for char in ransomNote:
        if char not in magazine_dict or magazine_dict[char] == 0:
            return False
        else:
            magazine_dict[char] -= 1

    return True
