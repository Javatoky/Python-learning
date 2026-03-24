"""Exercise 40 测试"""
import pytest
from exercise40 import MyRange


class TestMyRange:
    """MyRange 测试"""

    def test_basic(self):
        """单参数: MyRange(5) → 0,1,2,3,4"""
        assert list(MyRange(5)) == [0, 1, 2, 3, 4]

    def test_start_stop(self):
        """双参数: MyRange(2, 7) → 2,3,4,5,6"""
        assert list(MyRange(2, 7)) == [2, 3, 4, 5, 6]

    def test_with_step(self):
        """三参数: MyRange(0, 10, 3) → 0,3,6,9"""
        assert list(MyRange(0, 10, 3)) == [0, 3, 6, 9]

    def test_empty(self):
        """空范围"""
        assert list(MyRange(0)) == []
        assert list(MyRange(5, 3)) == []

    def test_reusable(self):
        """可重复遍历"""
        r = MyRange(3)
        assert list(r) == [0, 1, 2]
        assert list(r) == [0, 1, 2]  # 第二次依然有效

    def test_len(self):
        """长度计算"""
        assert len(MyRange(5)) == 5
        assert len(MyRange(2, 7)) == 5
        assert len(MyRange(0, 10, 3)) == 4
        assert len(MyRange(0)) == 0

    def test_repr(self):
        """字符串表示"""
        assert repr(MyRange(5)) == "MyRange(0, 5, 1)"
        assert repr(MyRange(1, 10, 2)) == "MyRange(1, 10, 2)"

    def test_step_zero_raises(self):
        """step=0 应报错"""
        with pytest.raises(ValueError):
            MyRange(0, 10, 0)

    def test_in_for_loop(self):
        """在 for 循环中使用"""
        result = []
        for x in MyRange(1, 6, 2):
            result.append(x * 10)
        assert result == [10, 30, 50]

    def test_next_manually(self):
        """手动调用 iter/next"""
        it = iter(MyRange(3))
        assert next(it) == 0
        assert next(it) == 1
        assert next(it) == 2
        with pytest.raises(StopIteration):
            next(it)