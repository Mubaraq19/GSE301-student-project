class DataSet:
    def __init__(self, data_file, category_file):
        self.data_file = data_file
        self.category_file = category_file
        self.data = []
        self.categories = set()
        self.total = 0
        self.average = 0
        self.minimum = None
        self.maximum = None
    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                lines = file.readlines()

                if len(lines) == 0:
                    raise ValueError("Data file is empty")

                for line in lines:
                    try:
                        value = float(line.strip())
                        self.data.append(value)
                    except ValueError:
                        print(f"Invalid value skipped: {line.strip()}")

            if len(self.data) == 0:
                raise ValueError("No valid numeric data found")

        except FileNotFoundError:
            print("Error: Data file does not exist.")
            exit()
        except ValueError as e:
            print("Error:", e)
            exit()
        try:
            with open(self.category_file, "r") as file:
                for line in file:
                    self.categories.add(line.strip())
        except FileNotFoundError:
            print("Warning: Category file not found.")
    def calculate_total(self, data):
        total = 0
        for value in data:
            total += value
        return total

    def calculate_average(self, total, count):
        return total / count

    def calculate_minimum(self, data):
        minimum = data[0]
        for value in data:
            if value < minimum:
                minimum = value
        return minimum

    def calculate_maximum(self, data):
        maximum = data[0]
        for value in data:
            if value > maximum:
                maximum = value
        return maximum

    def calculate_statistics(self):
        count = 0

        for _ in self.data:
            count += 1

        self.total = self.calculate_total(self.data)
        self.average = self.calculate_average(self.total, count)
        self.minimum = self.calculate_minimum(self.data)
        self.maximum = self.calculate_maximum(self.data)
        
    def display_results(self):
        print("Dataset:", self.data)
        print("Total:", self.total)
        print("Average:", self.average)
        print("Minimum:", self.minimum)
        print("Maximum:", self.maximum)

        if self.average >= 70:
            print("Performance: High Performance")
        else:
            print("Performance: Needs Improvement")

        print("Unique Categories:", self.categories)
        print("Number of Unique Categories:", len(self.categories))
        
    def save_report(self):
        with open("report.txt", "w") as file:
            file.write("DATASET ANALYSIS REPORT\n")
            file.write("-----------------------\n")
            file.write(f"Total: {self.total}\n")
            file.write(f"Average: {self.average}\n")
            file.write(f"Minimum: {self.minimum}\n")
            file.write(f"Maximum: {self.maximum}\n")
            file.write(f"Unique Categories Count: {len(self.categories)}\n")

dataset = DataSet("data.txt", "categories.txt")
dataset.load_data()
dataset.calculate_statistics()
dataset.display_results()
dataset.save_report()