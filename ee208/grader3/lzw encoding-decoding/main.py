def lzw_encode(input_string: str) -> list[int]:
    dictionary = {chr(i): i for i in range(256)}
    answer = []
    w = ""
    next_code = 256
    for c in input_string:
        wc = w+c
        if wc in dictionary.keys():
            w = wc
        else:
            answer.append(dictionary[w])
            dictionary[wc] = next_code
            next_code += 1
            w = c
    if w != "":
        answer.append(dictionary[w])
    return answer 
def lzw_decode(encoded_input: list[int]) -> str:
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    text = ""
    k = encoded_input[0]
    w = dictionary[k]
    text += w
    for k in encoded_input[1:]:
        if k in dictionary.keys():
            entry = dictionary[k]
        else:
            entry = w + w[0]
        text += entry            
        dictionary[next_code] = w + entry[0]
        next_code += 1
        w  = entry
        # print("Debug: ",w,entry, text)
        
    return text    
if __name__ == "__main__":  
    original_string = "TOBEORNOTTOBEORTOBEORNOT"
    encoded = lzw_encode(original_string)
    print("Encoded:", encoded)
    decoded = lzw_decode(encoded)
    print("Decoded:", decoded)
    assert original_string == decoded
    print("Original length:", len(original_string))
    print("Encoded length:", len(encoded))