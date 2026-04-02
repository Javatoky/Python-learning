"""Exercise 50 测试"""
import asyncio

import pytest
from exercise50 import AsyncCounter, AsyncDatabase


class TestAsyncDatabase:

    @pytest.mark.asyncio
    async def test_basic_usage(self, capsys):
        async with AsyncDatabase("test.db") as db:
            result = await db.execute("SELECT 1")
            assert result == "SELECT 1 → ok"
            assert db.connected is True

        output = capsys.readouterr().out
        assert "连接到 test.db" in output
        assert "断开 test.db" in output

    @pytest.mark.asyncio
    async def test_queries_recorded(self):
        async with AsyncDatabase("test.db") as db:
            await db.execute("SELECT 1")
            await db.execute("SELECT 2")
            assert db.queries == ["SELECT 1", "SELECT 2"]

    @pytest.mark.asyncio
    async def test_disconnected_after_exit(self):
        async with AsyncDatabase("test.db") as db:
            pass
        assert db.connected is False

    @pytest.mark.asyncio
    async def test_exception_still_disconnects(self):
        with pytest.raises(RuntimeError):
            async with AsyncDatabase("test.db") as db:
                raise RuntimeError("boom")
        assert db.connected is False


class TestAsyncCounter:

    @pytest.mark.asyncio
    async def test_basic(self):
        results = []
        async for num in AsyncCounter(1, 5):
            results.append(num)
        assert results == [1, 2, 3, 4]

    @pytest.mark.asyncio
    async def test_empty(self):
        results = []
        async for num in AsyncCounter(5, 5):
            results.append(num)
        assert results == []

    @pytest.mark.asyncio
    async def test_single(self):
        results = []
        async for num in AsyncCounter(0, 1):
            results.append(num)
        assert results == [0]

    @pytest.mark.asyncio
    async def test_concurrent_counters(self):
        """两个计数器并发运行"""
        async def collect(start, stop):
            return [num async for num in AsyncCounter(start, stop)]

        r1, r2 = await asyncio.gather(
            collect(1, 4),
            collect(10, 13),
        )
        assert r1 == [1, 2, 3]
        assert r2 == [10, 11, 12]