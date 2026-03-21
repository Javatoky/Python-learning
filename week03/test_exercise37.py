from exercise37 import chunk_iter, fibonacci_gen, square_seven_multiple

"""练习测试"""


def test_fibonacci_gen(n = 8, expect = [1, 1, 2, 3, 5, 8, 13, 21]):
    test_values = []
    for value in fibonacci_gen(8):
        test_values.append(value)
    assert test_values == expect

def test_chunk_iter(item = [1,2,3,4,5,6,7], size = 3):
    test_chunks = []
    for chunk in chunk_iter(item, size):
        test_chunks.append(chunk)
    assert test_chunks == [[1,2,3], [4,5,6], [7]]

def test_square_seven_multiple():
    assert next(square_seven_multiple) == 49

