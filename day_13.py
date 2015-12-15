import re
import itertools

test_input = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""


def parse_input(input):
    c = re.compile("""(?P<person_a>\w+)\swould\s
                            (?P<change>(?:gain|lose))\s
                            (?P<number>\d+)\s
                            happiness\sunits\sby\ssitting\snext\sto\s
                            (?P<person_b>\w+)\.""", re.X)
    return c.search(input).groupdict()


class Happyness(object):
    changes = {
        'gain': lambda x: x,
        'lose': lambda x: -x
    }

    def __init__(self, person_a, person_b, change, number):
        self.person_a = person_a
        self.person_b = person_b
        self.number = int(number)
        self._change = change

    @property
    def change(self):
        return self.changes[self._change](self.number)

    @property
    def names(self):
        return (self.person_a, self.person_b)


class TableSeating(list):
    def __init__(self):
        self.unique_names = set()

    @classmethod
    def add_by_inputs(cls, inputs):
        self = cls()
        for input in inputs:
            self.unique_names.add(input.get('person_a'))
            self.unique_names.add(input.get('person_b'))
            self.append(Happyness(**input))
        return self

    def add_me(self):
        for name in self.unique_names:
            self.append(Happyness(person_a="Ryan", person_b=name, change="gain", number=0))
            self.append(Happyness(person_a=name, person_b="Ryan", change="gain", number=0))
        self.unique_names.add("Ryan")

    def get_by_names(self, person_a, person_b):
        for item in self:
            if item.names == (person_a, person_b):
                return item
        return None

    def best_arrangement(self):
        to_ret = []
        arrangements = itertools.permutations(self.unique_names)
        for arrangement in arrangements:
            to_ret.append((arrangement, self._get_sum(arrangement)))
        return to_ret

    def _get_sum(self, names):
        sum = self.get_by_names(names[0], names[-1]).change
        sum += self.get_by_names(names[-1], names[0]).change

        for i in range(len(names) - 1):
            # print "getting", names[i], names[i+1]
            sum += self.get_by_names(names[i], names[i+1]).change
            sum += self.get_by_names(names[i+1], names[i]).change
        return sum



# test_input = test_input.splitlines()

# test_inputs = TableSeating.add_by_inputs(map(parse_input, test_input))

# test_inputs.best_arrangement()


with open('day_13.txt', 'r') as f:
    input = f.read().splitlines()

inputs = TableSeating.add_by_inputs(map(parse_input, input))

bests =  inputs.best_arrangement()
print max(bests, key=lambda k: k[1])

inputs.add_me()
bests =  inputs.best_arrangement()
print max(bests, key=lambda k: k[1])



