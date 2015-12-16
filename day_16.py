import re


class Sue(object):
    def __init__(self):
        self.traits = {}

    @classmethod
    def add_by_attributes(cls, name, *args, **kwargs):
        self = cls()
        self.name = name
        for key, value in kwargs.iteritems():
            self.traits[key] = int(value)
        return self

    def __repr__(self):
        return "Sue(<%s>)" % self.name

    def compare(self, real_sue):
        fail = False
        for trait, value in self.traits.iteritems():
            if value != real_sue.traits.get(trait):
                fail = True
        return not fail

    def compare_again(self, real_sue):
        fail = False
        for trait, value in self.traits.iteritems():
            if trait in ['trees', 'cats']:
                if value <= real_sue.traits.get(trait):
                    fail = True
            elif trait in ['pomeranians', 'goldfish']:
                if value >= real_sue.traits.get(trait):
                    fail = True
            else:
                if value != real_sue.traits.get(trait):
                    fail = True
        return not fail


real_sue = Sue.add_by_attributes("Real Sue", **{"children": 3,
                                                "cats": 7,
                                                "samoyeds": 2,
                                                "pomeranians": 3,
                                                "akitas": 0,
                                                "vizslas": 0,
                                                "goldfish": 5,
                                                "trees": 3,
                                                "cars": 2,
                                                "perfumes": 1})


def parser():
    with open('day_16.txt', 'r') as f:
        sues = [i for i in f.read().split('\n') if i]
    to_ret = []
    for sue in sues:
        search = re.search(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', sue)
        attrs = {
            search.group(2): search.group(3),
            search.group(4): search.group(5),
            search.group(6): search.group(7),
        }
        to_ret.append(
            Sue.add_by_attributes(search.group(1), **attrs)
        )
    return to_ret

all_the_sues = parser()
print [i for i in map(lambda x: (x.name, x.compare(real_sue)), all_the_sues) if i[1]]
print [i for i in map(lambda x: (x.name, x.compare_again(real_sue)), all_the_sues) if i[1]]
