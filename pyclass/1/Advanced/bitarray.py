

def ceiling_division(eggs, carton_size):
    '''Return the number of containers required to hold a given number of elements

       # It takes two carton of size one dozen to hold 14 eggs
       >>> ceiling_division(eggs=14, carton_size=12)
       2
       
    '''
    return -(-eggs // carton_size)

BITS_IN_BYTE = 8

class BitArray(object):
    'Space-efficient bit array built on top of a bytearray'

    def __init__(self, numbits):
        self.numbits = numbits
        numbytes = ceiling_division(numbits, BITS_IN_BYTE)
        self.data = bytearray(numbytes)

    def __len__(self):
        return self.numbits

    def _validate_index(self, index):
        if index < 0:
            index += len(self)
        if index >= len(self) or index < 0:
            raise IndexError("bitarray index out of array")
        return index

    def __getitem__(self, index):
        index = self._validate_index(index)
        bytenum, bitnum = divmod(index, BITS_IN_BYTE)
        return (self.data[bytenum] >> bitnum) & 1

    def __setitem__(self, index, value):
        index = self._validate_index(index)
        if value not in (0, 1):
            raise ValueError("bit must be in range (0, 2)")
        bytenum, bitnum = divmod(index, BITS_IN_BYTE)
        mask = 1 << bitnum
        if value:
            self.data[bytenum] |= mask
        else:
            self.data[bytenum] &= ~mask

    def __repr__(self):
        data = ''.join(map(str, self))
        if len(self) > 100:
            data = data[:100] + '...'
        return '{0.__class__.__name__}({1!r})'.format(self, data)

if __name__ == '__main__':
    b = BitArray(20)
    b[11] = 1
    b[14] = 1
    b[7] = 1
    print list(b.data)
