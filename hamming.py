def distance(strand_a, strand_b):

    if len(strand_a)!=len(strand_b):
        raise Exception("The strands are not equal in length!")

    distance = 0 
    valid_dna_letters = ['C','A','G','T']

    for i in range(0,len(strand_a)):
        
        if (strand_a[i] in valid_dna_letters) & (strand_b[i] in valid_dna_letters):
            if strand_a[i] != strand_b[i]:
                #distance = distance + 1
                distance += 1
    
    return distance
   


# if __name__ == "__main__":
#     print(distance("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"))