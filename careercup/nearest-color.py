# https://www.careercup.com/question?id=5633403314503680
# #RRGGBB -> #RGB

def shorten(color):
    color = int(color, 16)
    lower = (color / 0x11) * 0x11
    higher = ((color / 0x11) + 1) * 0x11

    if (color - lower) < (higher - color):
        return hex(lower)[3]
    else:
        return hex(higher)[3]

def nearest_short_color(long_color):
    red = shorten(long_color[1:3])
    green = shorten(long_color[3:5])
    blue = shorten(long_color[5:7])

    return '#{}{}{}'.format(red, green, blue)


if __name__ == '__main__':
    print nearest_short_color('#09f166')


