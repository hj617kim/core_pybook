def my_count(seq, item, is_str = True) :
    count = 0
    if is_str :
        for i in range(len(seq) - len(item) + 1) :
            if seq[i : i + len(item)] == item :
                count += 1
    else :
        for i in seq :
            if i == item :
                count += 1
    return count


def my_zip(*iterables) :
    iterators = [iter(it) for it in iterables]
    while True :
        try : 
            result = []
            for it in iterators :
                result.append(next(it))
            yield tuple(result)
        except StopIteration:
            return

print(my_count('helheloh', 'lh'))
print(my_count((1, 3, 5, 3, 5, 7), 3, is_str = False))

my_iter = my_zip([1, 2, 3], (1, 2), range(5))
print(next(my_iter))
print(next(my_iter))
