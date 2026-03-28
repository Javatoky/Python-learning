"""Exercise 44 测试"""
import os
from pathlib import Path

import pytest
from exercise44 import temp_workspace


class TestTempWorkspace:
    """temp_workspace 测试"""

    def test_creates_temp_dir(self):
        """创建临时目录"""
        with temp_workspace() as tmpdir:
            assert tmpdir.exists()
            assert tmpdir.is_dir()

    def test_changes_working_dir(self):
        """切换工作目录"""
        original = Path.cwd()
        with temp_workspace() as tmpdir:
            assert Path.cwd() == tmpdir
        assert Path.cwd() == original

    def test_can_create_files_inside(self):
        """可以在临时目录中创建文件"""
        with temp_workspace() as tmpdir:
            test_file = tmpdir / "test.txt"
            test_file.write_text("hello", encoding="utf-8")
            assert test_file.exists()

    def test_cleanup_after_exit(self):
        """退出后自动清理"""
        saved_path = None
        with temp_workspace() as tmpdir:
            saved_path = tmpdir
            (tmpdir / "file.txt").write_text("data", encoding="utf-8")
        assert not saved_path.exists()

    def test_restores_dir_on_exception(self):
        """异常时也恢复目录"""
        original = Path.cwd()
        with pytest.raises(RuntimeError):
            with temp_workspace() as tmpdir:
                raise RuntimeError("boom")
        assert Path.cwd() == original

    def test_cleanup_on_exception(self):
        """异常时也清理临时目录"""
        saved_path = None
        with pytest.raises(RuntimeError):
            with temp_workspace() as tmpdir:
                saved_path = tmpdir
                raise RuntimeError("boom")
        assert not saved_path.exists()

    def test_prefix(self):
        """自定义前缀"""
        with temp_workspace(prefix="myproject") as tmpdir:
            assert "myproject" in tmpdir.name