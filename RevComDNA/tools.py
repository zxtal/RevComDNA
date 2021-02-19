class DnaSequenceManipulator:
    """
    Represent a collection of tools to manipulate a given DNA sequence.
    """

    def __init__(self, sequence):
        """
        Initialise a DNA manipulator object. Taking the supplied DNA sequence, sequence, string as object attribute.
        """
        self.sequence = sequence.upper()

    def reverse_sequence(self) -> str:
        """
        calculate and return the reverse sequence of the supplied DNA sequence.

        """
        return self.sequence[::-1]

    def complement_sequence(self) -> str:
        """
        calculate and return the complementary sequence of the supplied DNA sequence.
        :return:
        """
        complementary = ""
        nucleotides_matching_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}

        for nucleotide in self.sequence:
            if nucleotide in nucleotides_matching_dict.keys():
                complementary += nucleotides_matching_dict.get(nucleotide)

        return complementary

    def reverse_complement_sequence(self) -> str:
        """
        calculate and return the reverse complement sequence of the supplied DNA sequence.
        """
        self.sequence = self.complement_sequence()
        reverse_complementary = self.reverse_sequence()

        return reverse_complementary
