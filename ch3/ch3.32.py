def hamming_distance(string_1:str, string_2:str):
    distance = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            distance += 1
    return distance
print(hamming_distance("strong", "strugg"))
