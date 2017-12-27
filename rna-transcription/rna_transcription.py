def to_rna(dna_strand):
    dna_to_rna_dictionary = {"A": "U", "C": "G", "G": "C", "T": "A"}
    try:
        rna_transcription = ''.join([dna_to_rna_dictionary[nucletoide] for nucletoide in dna_strand])
        return rna_transcription
    except:
        raise ValueError('Incorrect value to transcript RNA')
