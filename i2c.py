# I2C wrapper

from smbus import SMBus

bus = SMBus(1)


class I2C:
    def __init__(self, addr, bus_addr=1):
        self.addr = addr
        self.bus = SMBus(bus_addr)

    def write_byte(self, data, reg=None):
        if reg is None:
            bus.write_byte(self.addr, data)
        else:
            bus.write_byte_data(self.addr, reg, data)

    def write_bytes(self, data, reg):
        bus.write_block_data(self.addr, reg, bytes)

    def write_bits(self, data, reg, pos, mask=None):
        if data << pos > 0xFF:
            raise ValueError("Tried to set higher bit than 7")

        val = self.read_bytes(reg)

        if mask is None:
            val &= ~(1 << pos)
        else:
            val &= ~mask

        val |= data << pos

        self.write_byte(val, reg)

    def read_byte(self, reg=None):
        if reg is None:
            return bus.read_byte(self.addr)
        else:
            return bus.read_byte_data(self.addr, reg)

    def read_bytes(self, reg, len):
        bus.read_i2c_block_data(self.addr, reg, len)
