import ctypes
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self):
        return self.n

    def append(self, val):
        if self.capacity == self.n:
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size

    def __getitem__(self,ind):
        if ind >= 0:
            if ind <= self.n - 1:
                return self.data_arr[ind]
            else:
                raise IndexError("Out of range!")
        if ind < 0:
            if abs(ind) <= self.n:
                ind += self.n
                return self.data_arr[ind]
            else:
                raise IndexError("Out of range!")

    def __setitem__(self, ind, val):
        if not(self.n - 1 >= ind >= 0):
            raise IndexError("Invalid index")
        self.data_arr[ind] = val

    def  __iter__(self):
        for i in range(self.n + 1):
            yield self.data_arr[i]

    def extend(self, other_collection):
        for elem in other_collection:
            self.append(elem)

    def insert(self, index, val):
        if self.capacity == self.n:
            self.resize(2 * self.capacity)
        for i in range(self.n - 1, index - 1, -1):
            self.data_arr[i + 1] = self.data_arr[i]
        self.data_arr[index] = val
        self.n += 1
    def pop(self, k = -1):
        if self.n == 0:
            raise IndexError("This is an empty list")
        if k >= 0:
            if k < self.n:
                temp = self.data_arr[k]
                for i in range(k, self.n - 1):
                    self.data_arr[i] = self.data_arr[i + 1]
                self.n -= 1
                return temp
            else:
                raise IndexError("Out of range!")
        if k < -1:
            if abs(k) <= self.n + 1:
                temp = self.data_arr[k + self.n]
                for i in range(k + self.n, self.n - 1):
                    self.data_arr[i] = self.data_arr[i + 1]
                self.n -= 1
                return temp
            else:
                raise IndexError("Out of range!")
        if k == -1:
            temp = self.data_arr[self.n - 1]
            self.data_arr[self.n - 1] = None
            self.n -= 1
            return temp

    def __repr__(self):
        final_str = "["
        for i in range(self.n):
            final_str += str(self.data_arr[i]) + ","
        final_lst = final_str[:-1] + "]"
        return final_lst
