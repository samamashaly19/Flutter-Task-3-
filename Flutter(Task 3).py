def caesar_cipher(n, s, k):
   
    k = k % 26
    encrypted_string = []

    for char in s:
        if 'a' <= char <= 'z':  
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            encrypted_string.append(new_char)
        elif 'A' <= char <= 'Z':  
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            encrypted_string.append(new_char)
        else:
            
            encrypted_string.append(char)

    return ''.join(encrypted_string)


if __name__ == "__main__":
    n = int(input().strip())  
    s = input().strip()       
    k = int(input().strip())   
    result = caesar_cipher(n, s, k)
    print(result)
