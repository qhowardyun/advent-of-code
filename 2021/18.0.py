from aocd import get_data, submit
import io
import copy


class Node:
    def __init__(self, left=None, right=None):
        self.l = left
        self.r = right
        self.p = None

    def __deepcopy__(self, memo):
        a = copy.deepcopy(self.l)
        b = copy.deepcopy(self.r)
        n = Node(a, b)
        if isinstance(a, Node):
            a.p = n
        if isinstance(b, Node):
            b.p = n
        return n

    @staticmethod
    def from_str(ds: io.StringIO):
        char = ds.read(1)

        if char.isdigit():
            return int(char)
        else:
            l = Node.from_str(ds)
            ds.read(1)  # read comma
            r = Node.from_str(ds)
            ds.read(1)  # read ]

            n = Node(l, r)
            if isinstance(l, Node):
                l.p = n
            if isinstance(r, Node):
                r.p = n
            return n

    def __str__(self):
        return f"({str(self.l)},{str(self.r)})"

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __add__(self, other):
        a = copy.deepcopy(self)
        b = copy.deepcopy(other)
        n = Node(a, b)
        a.p = n
        b.p = n
        n.simplify()
        return n

    def add_to_successor(self, num):
        last = self
        cur = self.p

        while cur.r == last:
            last = cur
            cur = cur.p
            if cur is None:
                return

        if isinstance(cur.r, Node):
            cur = cur.r
            while True:
                if isinstance(cur.l, Node):
                    cur = cur.l
                else:
                    cur.l += num
                    break
        else:
            cur.r += num

    def add_to_predecessor(self, num):
        last = self
        cur = self.p

        while cur.l == last:
            last = cur
            cur = cur.p
            if cur is None:
                return

        if isinstance(cur.l, Node):
            cur = cur.l
            while True:
                if isinstance(cur.r, Node):
                    cur = cur.r
                else:
                    cur.r += num
                    break
        else:
            cur.l += num

    @staticmethod
    def explode(n, d=0):
        if d >= 4 and isinstance(n.l, int) and isinstance(n.r, int):
            l, r = n.l, n.r
            n.add_to_predecessor(l)
            n.add_to_successor(r)
            return True, False

        if isinstance(n.l, Node):
            clear, sd = Node.explode(n.l, d + 1)
            if clear:
                n.l = 0

            if not sd:
                return False, False

        if isinstance(n.r, Node):
            clear, sd = Node.explode(n.r, d + 1)
            if clear:
                n.r = 0

            if not sd:
                return False, False

        return False, True

    @staticmethod
    def split(n):

        if isinstance(n, Node):
            n.l, done = Node.split(n.l)
            if isinstance(n.l, Node):
                n.l.p = n
            if not done:
                return n, False

            n.r, done = Node.split(n.r)
            if isinstance(n.r, Node):
                n.r.p = n
            if not done:
                return n, False
            return n, True
        else:
            if n >= 10:
                return Node(n // 2, n - (n // 2)), False
            else:
                return n, True

    def simplify(self):
        while True:
            if not Node.explode(self)[1]:
                continue

            if not Node.split(self)[1]:
                continue

            break

    def magnitude(self):
        ml = self.l if isinstance(self.l, int) else self.l.magnitude()
        mr = self.r if isinstance(self.r, int) else self.r.magnitude()
        return ml * 3 + mr * 2


day = 18
data = get_data(day=day, year=2021)
lines = data.splitlines()
ans = 0

nums = []

for line in lines:
    ds = io.StringIO(line)
    nums.append(Node.from_str(ds))

ans = sum(nums)
print(ans.magnitude())
submit(ans.magnitude(), part="a", day=day, year=2021, reopen=False)

ans = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            s = nums[i] + nums[j]
            ans = max(ans, s.magnitude())

print(ans)
submit(ans, part="b", day=day, year=2021, reopen=False)
