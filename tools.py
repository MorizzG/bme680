# BME680 tools


def twos_comp(val, bits=16):
    """Convert two bytes into a two's compliment signed word."""
    if val & (1 << (bits - 1)) != 0:
        val = val - (1 << bits)
    return val


def bytes_to_word(msb, lsb, bits=16, signed=False):
    """Convert a most and least significant byte into a word."""
    # TODO: Reimpliment with struct
    word = (msb << 8) | lsb
    if signed:
        word = twos_comp(word, bits)
    return word
