import sys

sys.stdin = open("../../_test/test.in", "r")
sys.stdout = open("../../_test/test.out", "w")
class BIT:
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (size + 1)
        self.arr = [0] * size

    def set(self, ind, val):
        self.add(ind, val - self.arr[ind])

    def add(self, ind, val):
        self.arr[ind] += val
        ind += 1
        while ind <= self.size:
            self.bit[ind] += val
            ind += ind & -ind

    def pref_sum(self, ind):
        ind += 1
        total = 0
        while ind > 0:
            total += self.bit[ind]
            ind -= ind & -ind
        return total


def euler_tour(at, prev):
    global timer
    start[at] = timer
    timer += 1
    for n in neighbors[at]:
        if n != prev:
            euler_tour(n, at)
    end[at] = timer


# Input Handling
if __name__ == "__main__":
    node_num, query_num = map(int, input().split())

    vals = list(map(int, input().split()))

    neighbors = [[] for _ in range(node_num)]
    for _ in range(node_num - 1):
        n1, n2 = map(int, input().split())
        neighbors[n1 - 1].append(n2 - 1)
        neighbors[n2 - 1].append(n1 - 1)

    start = [0] * node_num
    end = [0] * node_num
    timer = 0
    euler_tour(0, -1)

    bit = BIT(node_num)
    for i in range(node_num):
        bit.set(start[i], vals[i])

    for _ in range(query_num):
        query = list(map(int, input().split()))
        if query[0] == 1:
            node, val = query[1], query[2]
            bit.set(start[node - 1], val)
        elif query[0] == 2:
            node = query[1] - 1
            end_sum = bit.pref_sum(end[node] - 1)
            start_sum = bit.pref_sum(start[node] - 1) if start[node] > 0 else 0
            print(end_sum - start_sum)
