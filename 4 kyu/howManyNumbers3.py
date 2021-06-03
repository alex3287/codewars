def find_all(sum_dig, digs):
    if sum_dig / digs > 9:
        return []
    number = sum_dig // digs + sum_dig % digs
    k = digs * number
    return [k, 0, 0]