# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) in [0, 1]:
        return [sequence]
    else:
        perms = []
        for item in sequence:
            sub_seq = sequence.replace(item, '')
            sub_perms = get_permutations(sub_seq)
            for tmp_seq in sub_perms:
                perms.extend([tmp_seq[:idx]+item+tmp_seq[idx:] for idx in range(len(sub_seq)+1)])
        return list(set(perms))



if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print(set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])==set(get_permutations(example_input)))

    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(example_input))
    print(set(['ab', 'ba'])==set(get_permutations(example_input)))

    example_input = 'pow'
    print('Input:', example_input)
    print('Expected Output:', ['pow', 'pwo', 'opw', 'owp', 'wpo', 'wop'])
    print('Actual Output:', get_permutations(example_input))
    print(set(['pow', 'pwo', 'opw', 'owp', 'wpo', 'wop'])==set(get_permutations(example_input)))



