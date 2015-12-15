import collections, functools


def memoize(func):
    class memoize(dict):
        def __init__(self, func):
            self.func = func
            self.cache = {}

        def __call__(self, *args):
            if self.func not in self.cache:
                self.cache[self.func] = {}
            if not isinstance(args, collections.Hashable):
                return self.func(*args)
            if args in self.cache[self.func]:
                return self.cache[self.func][args]
            else:
                value = self.func(*args)
                self.cache[self.func][args] = value
                return value

        def __repr__(self):
            """Return the function's docstring."""
            return self.func.__doc__

        def __get__(self, obj, objtype):
            """Support instance methods."""
            fn = functools.partial(self.__call__, obj)
            try:
                self.cache = obj.cache
            except:
                self.cache = obj.cache = {}
            return fn
    return memoize(func)


class LogicGate:
    functions = {
        "IDENTITY": lambda x: x,
        "AND": lambda x, y: x & y,
        "OR": lambda x, y: x | y,
        "NOT": lambda x: ~x,
        "XOR": lambda x, y: x ^ y,
        "LSHIFT": lambda x, y: x << y,
        "RSHIFT": lambda x, y: x >> y,
    }

    def __init__(self, gate_type, pins):
        self.type = gate_type
        self.fn = self.functions[gate_type]
        self.pins = pins

    def _get_pin(self, pin, circuit):
        if pin.isdigit():
            return int(pin)
        else:
            return circuit.get_val(pin)

    def set_pin(self, val, pin):
        self.pins[pin] = val

    def _output(self, circuit):
        pins = [self._get_pin(p, circuit) for p in self.pins]
        if None not in pins:
            return self.fn(*pins)


class InstructionParser(object):
    def __init__(self, line_str):
        self.line_str = line_str

    def parse(self):
        instr, label = self.line_str.strip().split(" -> ")
        instr = instr.split()
        if len(instr) == 1:
            return (label, "IDENTITY", instr)
        elif len(instr) == 2:
            return (label, instr[0], [instr[1]])
        else:
            return (label, instr[1], [instr[0], instr[2]])


class ParseInstructions(list):
    @classmethod
    def get_by_input_string(cls, input):
        self = cls()
        self.extend(map(InstructionParser, input.split('\n')))
        return self


class LogicCircuit(object):
    def __init__(self):
        self._circuit = {}
        self.cache = {}

    def add_gate(self, label, type_, pins):
        self._circuit[label] = LogicGate(type_, pins)

    @memoize
    def get_val(self, gate):
        """Read output value from selected gate"""
        if gate in self._circuit:
            return self._circuit[gate]._output(self)
        else:
            return None

    def set_val(self, gate, val, pin=0):
        """Set gate pin to given value"""
        self.cache = {}
        g = self._circuit[gate]
        g.set_pin(val, pin)

if __name__ == '__main__':
    circuit = LogicCircuit()
    for ins in ParseInstructions.get_by_input_string(input):
        circuit.add_gate(*ins.parse())

    a = circuit.get_val("a")
    print "Part A:", a

    circuit.set_val("b", str(a))
    print "Part B", circuit.get_val("a")
