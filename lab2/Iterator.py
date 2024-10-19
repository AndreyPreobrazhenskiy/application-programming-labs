import csv

class Iterator:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.paths = self.__load__()
        self.limit = len(self.paths)
        self.counter = 0

    def __iter__(self) -> 'Iterator':
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            next_element = self.paths[self.counter]
            self.counter += 1
            return next_element
        else:
            raise StopIteration

    def __load__(self) -> list:
        """
        Reads a csv file specified by the filepath attribute and extracts the data from the second column of each row.
        :return: list of paths
        """
        with open(self.filepath, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            paths = [row[1] for row in reader]
            return paths