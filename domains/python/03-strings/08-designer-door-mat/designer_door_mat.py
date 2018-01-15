rows, columns = map(int, raw_input().split())
for upper_half_index in xrange(1, rows, 2):
    print upper_half_index * '.|.'
# print
# for lower_half_index in xrange(rows - 2, -1, -2):
#     print columns * '-'
