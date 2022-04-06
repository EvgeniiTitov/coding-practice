"""
Journal has got clear responsibilities.

Adding other methods such as saving/loading a journal would violate the
SOC principle.
The problem is if out application has, say, N objects and each implements its
own saving/loading/whatever, then if at some point we need to modify how those
objects are saved/loaded, then we'd need to go and modify it for each god damn
class --> extract the persistence logic to a separate class/module.

Anti-pattern God Object - does everything
"""


class Journal:
    def __init__(self):
        self.entires = []
        self.count = 0

    def add_entry(self, text):
        self.entires.append(text)
        self.count += 1

    def remove_entry(self, index):
        self.entires.pop(index)

    def __str__(self) -> str:
        return "; ".join(self.entires)


class PersistenceManager:
    @staticmethod
    def save_to_disk(obj, filename):
        with open(filename, "w") as file:
            file.write(str(obj))
        print("Saved file as:", filename)


def main():
    j = Journal()
    j.add_entry("Entry 1")
    j.add_entry("Entry 2")
    print(j)
    j.remove_entry(0)
    print(j)

    PersistenceManager.save_to_disk(j, "journal.txt")


if __name__ == "__main__":
    main()
