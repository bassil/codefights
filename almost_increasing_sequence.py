def almostIncreasingSequence(sequence):
    errors = []
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            errors.append(i)
            if len(errors) > 2:
                return False
    if len(errors) < 1:
        return True
    for error in errors:
        new_sequence = sequence[:error] + sequence[error+1:]
        for i in range(len(sequence)-1):
            if sequence[i] >= sequence[i+1]:
                return False
        return True
    return False

#a = list(range(10))
#print(a[:6], a[7:])
sequences = [[1, 3, 2, 1], 
            [1, 3, 2],
             [1, 2, 1, 2]]
for sequence in sequences:
#    print(is_i_tester(sequence))
    print(almostIncreasingSequence(sequence))

    
