class Reindeer(object):
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest
        self._current_seconds = 0
        self.points = 0

    @property
    def distance_travelled(self):
        total_seconds = self._current_seconds
        if total_seconds < self.duration:
            return self.speed * total_seconds
        else:
            occurences = total_seconds / (self.rest + self.duration)
            time_left = total_seconds - ((self.rest + self.duration) * occurences)
            # print "time left", time_left
            if time_left >= self.duration:
                occurences += 1
            distance = (occurences * self.speed * self.duration)
            if self._current_seconds > (occurences * (self.rest + self.duration)):
                distance += (time_left * self.speed)
            return distance

class Reindeers(list):
    @classmethod
    def add_by_reindeer(cls):
        self = cls()
        self.append(Reindeer('Vixen', 19, 7, 124))
        self.append(Reindeer('Rudolph', 3, 15, 28))
        self.append(Reindeer('Donner', 19, 9, 164))
        self.append(Reindeer('Blitzen', 19, 9, 158))
        self.append(Reindeer('Comet', 13, 7, 82))
        self.append(Reindeer('Cupid', 25, 6, 145))
        self.append(Reindeer('Dasher', 14, 3, 38))
        self.append(Reindeer('Dancer', 3, 16, 37))
        self.append(Reindeer('Prancer', 25, 6, 143))
        # self.append(Reindeer('Comet', 14, 10, 127))  # testing
        # self.append(Reindeer('Dancer', 16, 11, 162))  # testing

        return self

    def _get_by_name(self, name):
        for r in self:
            if r.name == name:
                return r

    def _reset_all(self):
        for reindeer in self:
            reindeer._current_seconds = 0
            reindeer.points = 0

    def _increment_by_second(self):
        for reindeer in self:
            reindeer._current_seconds += 1

    def _current_leaders(self):
        top_distance = max([r.distance_travelled for r in self])
        return [r for r in self if r.distance_travelled == top_distance]

    def _set_points_for_leader(self):
        for r in self._current_leaders():
            r.points += 1

    def stats_after_seconds(self, seconds):
        self._reset_all()
        for i in range(0, seconds):
            self._increment_by_second()
            self._set_points_for_leader()
        print "#" * 10
        print "Winner by distance"
        print "#" * 10, "\n\n"
        for r in sorted(self, key=lambda r : r.distance_travelled, reverse=True):
            print r.name, r.distance_travelled

        print "\n\n", "#" * 10
        print "Winner by points"
        print "#" * 10, "\n\n"
        for r in sorted(self, key=lambda r : r.points, reverse=True):
            print r.name, r.points




r = Reindeers.add_by_reindeer()
r.stats_after_seconds(2503)
