"""Exercise 49 测试"""
import asyncio
import time

import pytest
from exercise49 import (batch_process, batch_process_with_limit,
                        process_document)


class TestProcessDocument:

    @pytest.mark.asyncio
    async def test_returns_result(self):
        result = await process_document("test.txt", 0.1)
        assert result == {"doc": "test.txt", "time": 0.1, "status": "done"}

    @pytest.mark.asyncio
    async def test_output(self, capsys):
        await process_document("demo.md", 0.1)
        output = capsys.readouterr().out
        assert "[开始] demo.md" in output
        assert "[完成] demo.md" in output


class TestBatchProcess:

    @pytest.mark.asyncio
    async def test_processes_all(self):
        docs = [("a.txt", 0.1), ("b.txt", 0.1), ("c.txt", 0.1)]
        results = await batch_process(docs)
        assert len(results) == 3
        names = [r["doc"] for r in results]
        assert sorted(names) == ["a.txt", "b.txt", "c.txt"]

    @pytest.mark.asyncio
    async def test_concurrent_faster(self):
        """并发应该比顺序快"""
        docs = [("a.txt", 0.3), ("b.txt", 0.3), ("c.txt", 0.3)]
        start = time.perf_counter()
        await batch_process(docs)
        elapsed = time.perf_counter() - start
        # 并发执行应该约 0.3s，而非 0.9s
        assert elapsed < 0.6

    @pytest.mark.asyncio
    async def test_empty_list(self):
        results = await batch_process([])
        assert results == []


class TestBatchProcessWithLimit:

    @pytest.mark.asyncio
    async def test_respects_limit(self):
        """限流：最多同时 2 个"""
        docs = [("a.txt", 0.2), ("b.txt", 0.2), ("c.txt", 0.2), ("d.txt", 0.2)]
        start = time.perf_counter()
        results = await batch_process_with_limit(docs, max_concurrent=2)
        elapsed = time.perf_counter() - start

        assert len(results) == 4
        # 4个任务，每次最多2个并发，每批0.2s → 至少0.4s
        assert elapsed >= 0.35

    @pytest.mark.asyncio
    async def test_all_complete(self):
        docs = [("x.txt", 0.1), ("y.txt", 0.1)]
        results = await batch_process_with_limit(docs, max_concurrent=1)
        assert len(results) == 2

    @pytest.mark.asyncio
    async def test_limit_one_is_sequential(self):
        """max_concurrent=1 等价于顺序执行"""
        docs = [("a.txt", 0.15), ("b.txt", 0.15), ("c.txt", 0.15)]
        start = time.perf_counter()
        await batch_process_with_limit(docs, max_concurrent=1)
        elapsed = time.perf_counter() - start
        # 顺序: 约 0.45s
        assert elapsed >= 0.4