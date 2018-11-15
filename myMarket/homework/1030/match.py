for a in range(ord('x'),ord('z') + 1):
    for b in range(ord('x'),ord('z') + 1):
        if (a != b):
            for c in range(ord('x'),ord('z') + 1):
                if (a != c) and (b != c):
                    if a != ord('x') and c != ('x') and c != ord('z'):
                        print('a---%s' %chr(a))
                        print('b---%s' %chr(b))
                        print('c---%s' %chr(c))
