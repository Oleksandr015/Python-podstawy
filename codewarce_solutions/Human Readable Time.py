def make_readable(seconds):
    return '{:02}:{:02}:{:02}'.format(seconds // 3600, seconds % 3600 // 60, seconds % 60)


if __name__ == '__main__':
    print(make_readable(399))


#  return "%02d:%02d:%02d" % (h, m, s)