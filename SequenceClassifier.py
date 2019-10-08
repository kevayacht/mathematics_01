import csv
import os


class SequenceClassifier:
    """
    Instantiate the Sequence Classifier Class as specified
    """

    def __init__(self, file_path):
        """
        Instance attributes initialization method
        """
        self.count = 0
        self.file_path = file_path
        self.dirname = os.path.dirname(self.file_path) + '/'
        self.naturals = []
        self.odds = []
        self.evens = []
        self.fibonacci = []
        self.unclassified = []
        self.sub_sequence = []
        self.sequences = {
            "naturals": self.naturals,
            "odds": self.odds,
            "evens": self.evens,
            "fibonacci": self.fibonacci,
            "unclassified": self.unclassified,  # could probably be removed.
        }
        self.manager()

    def manager(self):
        """
        Class method managing the sequence of events.
        @:param self: class instance
        :return: None
        """
        self.file_reader()
        self.export_data()

        # Printing data
        # print("total: %d" % self.count)
        # print("self.unclassified: %d" % len(self.unclassified))
        # print("self.naturals: %d" % len(self.naturals))
        # print("self.odds: %d" % len(self.odds))
        # print("self.evens: %d" % len(self.evens))
        # print("self.fibonacci: %d" % len(self.fibonacci))

    def file_reader(self):
        """
        Class method, Inserted datafile read method.
        :return: None
        """
        with open(self.file_path, 'r') as f:
            for self.count, line in enumerate(f):
                self.sub_sequence = line.strip("\n").split(",")
                self.sequencer()

    def sequencer(self):
        """
        Class method, single sub sequence classification method.
        :param self: class instance
        :return: None
        """
        # classifies if sub_sequence is natural
        nat = self.natural_check(self.sub_sequence)
        if nat:
            self.naturals.append(self.sub_sequence)

        # classifies if sub_sequence is odds
        odd = self.odds_check(self.sub_sequence)
        if odd:
            self.odds.append(self.sub_sequence)

        # classifies if sub_sequence is evens
        even = self.evens_check(self.sub_sequence)
        if even:
            self.evens.append(self.sub_sequence)

        # classifies if sub_sequence is fibonacci
        fib = self.fibonacci_check(self.sub_sequence)
        if fib:
            self.fibonacci.append(self.sub_sequence)

        # classifies if sub_sequence is unclassified for some reason.
        if not (nat or odd or even or fib):
            self.unclassified.append(self.sub_sequence)

    @staticmethod
    def natural_check(sub_sequence):
        """
        Static Method to check if sequence is natural.
        @:param sub_sequence: list: the list being analysed
        :return: bool: indicates if input is a natural sequence
        """
        res = []
        for i in range(len(sub_sequence) - 1):
            if int(sub_sequence[i]) + 1 == int(sub_sequence[i + 1]):
                res.append(False)
            else:
                res.append(True)

        return not any(res)

    @staticmethod
    def odds_check(sub_sequence):
        """
        Static Method to check if sequence is odd.
        @:param sub_sequence: list: the list being analysed
        :return: bool: indicates if the input is a odds sequence
        """
        res = []
        for i in range(len(sub_sequence)):
            if int(sub_sequence[i]) % 2 != 0:
                res.append(False)
            else:
                res.append(True)

        return not any(res)

    @staticmethod
    def evens_check(sub_sequence):
        """
        Static Method to check if sequence is even.
        @:param sub_sequence: list: the list being analysed
        :return: bool: indicates if the input is a evens sequence
        """
        res = []
        for i in range(len(sub_sequence)):
            if int(sub_sequence[i]) % 2 == 0:
                res.append(False)
            else:
                res.append(True)

        return not any(res)

    @staticmethod
    def fibonacci_check(sub_sequence):
        """
        Static Method to check if sequence is fibonacci.
        @:param sub_sequence: list: the list being analysed
        :return: bool: indicates if the input is a fibonacci sequence
        """
        res = []
        for i in range(len(sub_sequence) - 2):
            if int(sub_sequence[i]) + int(sub_sequence[i + 1]) == int(sub_sequence[i + 2]):
                res.append(False)
            else:
                res.append(True)

        return not any(res)

    def export_data(self):
        """
        Method to export the data to separately named csv out files.
        @:param self: class instance
        :return: None
        """
        for key, value in self.sequences.items():
            with open(self.dirname + key + '.csv', mode='w') as file:
                writer = csv.writer(file)
                writer.writerows(value)
            file.close()


def main():
    """
    Main function to start up the class from this point. (Entry point)
    """
    SequenceClassifier('data/sub_sequences.csv.xls')


if __name__ == '__main__':
    main()
