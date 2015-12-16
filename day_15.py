import re
import itertools

class MathMachine(object):

    def __init__(self):
        self.combo_values = {}

    def add_combination(self, combination, pairs):
        self.combo_values[combination] = [zip(combination, pair) for pair in pairs]

    def combination_products(self, problem_two=False):
        to_ret = []
        for combo, values in self.combo_values.iteritems():
            # if combo == (44, 56):
            property_sums = map(self._multiply_pairs, values)
            property_sums = map(self._remove_negatives, property_sums)
            if problem_two:
                if not property_sums[-1] == 500:
                    continue
            # if reduce(lambda x,y: x*y, property_sums[:-1]) == 11171160:
            #     print combo,values, property_sums
            to_ret.append(reduce(lambda x,y: x*y, property_sums[:-1]))
        return to_ret

    def _remove_negatives(self, val):
        return val if val > 0 else 0

    def _multiply_pairs(self, list_pairs):
        total = 0
        for first, second in list_pairs:
            total += first*second
        return total


class Ingredient(object):
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

    def __repr__(self):
        return 'Ingredient(name=%s)' % self.name


def parse_ingredient(line):
    searcher = re.compile(r'(?P<name>\w+): capacity (?P<capacity>-?\d), durability (?P<durability>-?\d), flavor (?P<flavor>-?\d), texture (?P<texture>-?\d), calories (?P<calories>-?\d)')
    return searcher.search(line).groupdict()

input = """\
Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8"""

class Ingredients(list):
    def __init__(self):
        self._combinations = []

    @property
    def combinations(self):
        for i in range(0,100):
            for j in range(0,100-i):
                for k in range(0,100-i-j):
                    h = 100-i-j-k
                    yield (i,j,k,h)

    @classmethod
    def init(cls):
        self = cls()
        for line in input.split('\n'):
            self.append(Ingredient(**parse_ingredient(line)))
        return self

    def get_by_property(self, property):
        return [getattr(p, property) for p in self]

    def calculate_ammounts(self):
        math = MathMachine()
        for combination in self.combinations:
            math.add_combination(combination,
                [self.get_by_property(property_) for property_ in ('capacity', 'durability', 'flavor', 'texture', 'calories')]
            )
        return math



ingredients = Ingredients.init()
x =  ingredients.calculate_ammounts()
print max(x.combination_products())
print max(x.combination_products(True))

# ingredients = Ingredients()
# ingredients.append(Ingredient("Butterscotch", -1, -2, 6, 3, 8))
# ingredients.append(Ingredient("Cinnamon", 2, 3, -2, -1, 3))
# x =  ingredients.calculate_ammounts()
