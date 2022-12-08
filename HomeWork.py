# class MinStat:
#     def __init__(self):
#         self.numbers = []
    
#     def add_number(self, number):
#         self.numbers.append(int(number))
    
#     def result(self):
#         if len(self.numbers) > 0:
#             min_number = self.numbers[0]
#             for num in self.numbers:
#                 if num < min_number:
#                     min_number = num
#             return min_number
#         else:
#             return

# m = MinStat()
# m.add_number(16)
# m.add_number(25)
# m.add_number(78)
# m.add_number(36)
# m.add_number(55)
# m.add_number(22)
# print(m.result())

#---------------------------------------------------------------------------------------------------

# class MaxStat:
#     def __init__(self):
#         self.numbers = []
    
#     def add_number(self, number):
#         self.numbers.append(int(number))
    
#     def result(self):
#         if len(self.numbers) > 0:
#             max_number = self.numbers[0]
#             for num in self.numbers:
#                 if num > max_number:
#                     max_number = num
#             return max_number
#         else:
#             return

# m = MaxStat()
# m.add_number(16)
# m.add_number(25)
# m.add_number(78)
# m.add_number(36)
# m.add_number(55)
# m.add_number(22)
# print(m.result())

#---------------------------------------------------------------------------------------------------

# class AverageStat:
#     def __init__(self):
#         self.numbers = []
#         self.count = 0
    
#     def add_number(self, number):
#         self.numbers.append(int(number))
#         self.count += 1
    
#     def result(self):
#         if len(self.numbers) > 0:
#             summ = 0
#             for num in self.numbers:
#                 summ += num
#             return summ/self.count
#         else:
#             return

# m = AverageStat()
# m.add_number(16)
# m.add_number(25)
# m.add_number(78)
# m.add_number(36)
# m.add_number(55)
# m.add_number(22)
# print(m.result())

#---------------------------------------------------------------------------------------------------

#         my_dict = {a: list() for a in first_letter_name}

# class Table:

#     def __init__(self, rows, cols):
#         self.numbers = [[0 for j in range(cols)] for i in range(rows)]
#         self.rows = rows
#         self.cols = cols

#     def set_value(self, row, col, value):
#         self.numbers[row - 1][col - 1] = value

#     def get_value(self, row, col):
#         if 1 <= row <= self.rows:
#             return self.numbers[row - 1][col - 1]
#         else:
#             return

#     def n_rows(self):
#         return self.rows

#     def n_cols(self):
#         return self.cols

#     def delete_row(self, row):
#         self.numbers.pop(row-1)
#         self.rows -= 1

#     def delete_col(self, col):
#         for row in self.numbers:
#             row.pop(col - 1)
#         self.cols -= 1

#     def add_row(self, row):
#         self.numbers.insert(row - 1, [0 for i in range(self.cols)])
#         self.rows += 1

#     def add_col(self, col):
#         for row in self.numbers:
#             row.insert(col - 1, 0)
#         self.cols += 1

# t = Table(5, 5)
# print(f'{t.n_rows()}x{t.n_cols()}')
# print(*t.numbers, sep ="\n")
# print()

# t.set_value(1, 1, 1)
# t.set_value(1, 2, 2)
# t.set_value(1, 3, 3)
# t.set_value(1, 4, 4)
# t.set_value(1, 5, 5)
# t.set_value(2, 1, 6)
# t.set_value(2, 2, 7)
# t.set_value(2, 3, 8)
# t.set_value(2, 4, 9)
# t.set_value(3, 1, 1)
# t.set_value(3, 2, 2)
# t.set_value(3, 3, 3)
# t.set_value(3, 4, 4)
# t.set_value(3, 5, 5)
# t.set_value(4, 1, 6)
# t.set_value(4, 2, 7)
# t.set_value(4, 3, 8)
# t.set_value(4, 4, 9)
# t.set_value(5, 1, 1)
# t.set_value(5, 2, 2)
# t.set_value(5, 3, 3)
# t.set_value(5, 4, 4)
# t.set_value(5, 5, 5)
# print(f'{t.n_rows()}x{t.n_cols()}')
# print(*t.numbers, sep ="\n")
# print()

# t.delete_row(3)
# print(f'{t.n_rows()}x{t.n_cols()}')
# print(*t.numbers, sep ="\n")
# print()

# t.delete_col(3)
# print(f'{t.n_rows()}x{t.n_cols()}')
# print(*t.numbers, sep ="\n")
# print()

# t.add_row(3)
# print(f'{t.n_rows()}x{t.n_cols()}')
# print(*t.numbers, sep ="\n")
# print()

# t.add_col(2)
# print(f'{t.n_rows()}x{t.n_cols()}')
# print(*t.numbers, sep ="\n")
# print()