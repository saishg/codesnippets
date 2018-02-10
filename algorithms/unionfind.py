
N = 10
IDS = range(10)

def within_range(*args):
    for i in args:
        if i >= N or i < 0:
            print i, ": exceeds range"
            return False
    return True

def get_root(i):
    count = 0
    while IDS[i] != i:
        IDS[i] = IDS[IDS[i]]
        i = IDS[i]
        count += 1
    return count, i

def slow_union(p, q):
    if within_range(p, q):
        if not quick_connected(p, q):
            new_value = IDS[p]
            old_value = IDS[q]
            for index, value in enumerate(IDS):
                if value == old_value:
                    IDS[index] = new_value
        print IDS

def quick_connected(p, q):
    if within_range(p, q):
        if IDS[p] == IDS[q]:
            print p, q, ": are connected"
            return True
        else:
            print p, q, ": are NOT connected"
            return False
    return False


def quick_union(p, q):
    if within_range(p, q):
        IDS[p] = IDS[q]
        print IDS

def quick_union_optimized(p, q):
    if within_range(p, q):
        p_count, q_count = 0, 0
        p_count, p = get_root(p)
        q_count, q = get_root(q)
        if p_count < q_count:
            IDS[p] = IDS[q]
        else:
            IDS[q] = IDS[p]
        print IDS


def slow_connected(p, q):
    orig_p, orig_q = p, q
    if within_range(p, q):
        _, p = get_root(p)
        _, q = get_root(q)
        if p == q:
            print orig_p, orig_q, ": are connected"
            return True
        else:
            print orig_p, orig_q, ": are NOT connected"
            return False
    return False


#union, connected = slow_union, quick_connected
#union, connected = quick_union, slow_connected
union, connected = quick_union_optimized, slow_connected

if __name__ == '__main__':
    print IDS
    union(3, 4)
    union(0, 5)
    union(5, 6)
    union(1, 6)
    union(1, 2)
    union(8, 3)
    union(4, 9)
    union(7, 2)
    connected(1, 7)
    connected(0, 9)
