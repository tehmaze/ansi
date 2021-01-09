CSI = '\x1b['
OSC = '\x1b]'
BEL = '\a'


def sequence(letter, fields=1, default=[]):
    def _sequence(*values):
        output = list(values)
        if fields >= 0 and len(output) > fields:
            raise ValueError('Invalid number of fields, got %d expected %d' %
                (len(output), fields))

        while len(output) < fields and len(default) > len(output):
            output.append(fields[len(default) - 1])

        return ''.join([
            CSI,
            ';'.join(map(str, output)),
            letter,
        ])

    return _sequence

def osc(number):
    def _osc(*args, **kwargs):
        kwargs = ["%s=%s" % (k,v) for (k,v) in kwargs.items()]
        return ''.join([
            OSC,
            str(number),
            ';',
            ';'.join(list(args)+kwargs),
            BEL,
        ])
    return _osc
