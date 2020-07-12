# hash 函数需要一个 size 参数，扩容使用
# 列表中的值：目前看需要三个：key，value，delete
# shrink 数据量小于 size / 4
# expand 数据大于 size / 2


class Hash:
    def __init__(self, initial_size=8):
        self.curr_size = 0
        self.data = [(None, None, None) for _ in range(initial_size)]

    def __str__(self):
        return str([(i, j) for i, j, d in self.data if d != 1 and i])

    def shrink(self):
        tmp = [(None, None, None) for _ in range(int(len(self.data) / 2))]
        self.re_hash(tmp)

    def expend(self):
        tmp = [(None, None, None) for _ in range(len(self.data) * 2)]
        self.re_hash(tmp)

    def re_hash(self, tmp):
        for key, value, d in self.data:
            index = self.hash(key, len(tmp))
            while True:
                k, v, _ = tmp[index]
                if not k:
                    break
                else:
                    index = (index + 1) % len(tmp)
            tmp[index] = (key, value, d)
        self.data = tmp

    def add(self, key, value):
        index = self.hash(key, len(self.data))
        while True:
            k, v, d = self.data[index]
            if not k:
                break
            elif k == key or d:
                self.data[index] = (key, value, None)
                return
            else:
                index = (index + 1) % len(self.data)

        self.data[index] = (key, value, None)

        self.curr_size += 1
        if self.curr_size > len(self.data) / 2:
            self.expend()

    def hash(self, k, size):
        """
        :param k:
        :param m: size of the tale
        :return: k % m
        """
        return int(bin(int(''.join([str(ord(c)) for c in str(k)]))), base=2) % size

    def exist(self, key):
        index = self.hash(key, len(self.data))
        while True:
            k, v, d = self.data[index]
            if not k:
                return -1
            elif k == key and d != 1:
                return index
            else:
                index = (index + 1) % len(self.data)

    def get(self, key):
        index = self.exist(key)
        if index < 0:
            return index
        return self.data[index][1]

    def remove(self, key):
        index = self.exist(key)
        if index < 0:
            return -1
        k, v, d = self.data[index]
        self.data[index] = k, v, 1
        self.curr_size -= 1
        if self.curr_size < len(self.data) / 4:
            self.shrink()
        return index


h = Hash()
h.add("hello", 1)
h.add("hello2", 1)
h.add("hello3", 1)
h.add("hello4", 1)
h.add("hello5", 1)
print("hello 是否存在", h.exist("hello"))
print("hello4 的值为 ", h.get("hello4"))
print(h.remove("hello4"))
print(h.remove("hello3"))
print(h.remove("hello2"))

print("hash 表中的数据", h)
