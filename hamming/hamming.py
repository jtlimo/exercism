def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        return count_hamming_distance(list(strand_a), list(strand_b))
    else:
        raise(ValueError)

def count_hamming_distance(strand_a, strand_b):
    count = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            count += 1
    return count
