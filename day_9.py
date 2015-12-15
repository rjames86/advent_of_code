import itertools

input = """\
Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46"""


class InstructionParse(object):
    def __init__(self, input):
        self.input = input
        self._distances = {}
        self.cities = set()
        self.parse_input()

    def parse_input(self):
        for i in self.input.split('\n'):
            left_side, right_side = i.split(' = ')
            start, finish = left_side.split(' to ')
            self.cities.add(start)
            self.cities.add(finish)
            self._distances[(start, finish)] = int(right_side)

    def permutations(self):
        to_ret = []
        for perm in itertools.permutations(self.cities, len(self.cities)):
            distance = 0
            for index, city in enumerate(perm[:-1]):
                try:
                    distance += self._distances[(perm[index], perm[index + 1])]
                except:
                    distance += self._distances[(perm[index + 1], perm[index])]
            to_ret.append((perm, distance))
        return to_ret

    def shortest_distance(self):
        return min(self.permutations(), key=lambda p: p[1])

    def furthest_distance(self):
        return max(self.permutations(), key=lambda p: p[1])


if __name__ == '__main__':
    parsed = InstructionParse(input)
    # This whole parser is kinda gross, but it works
    print "shortest", parsed.shortest_distance()
    print "furthest_distance", parsed.furthest_distance()
