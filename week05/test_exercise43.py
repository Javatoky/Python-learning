"""Exercise 43 测试"""
import pytest
from exercise43 import DatabaseConnection


class TestDatabaseConnection:
    """DatabaseConnection 测试"""

    def test_normal_flow(self, capsys):
        """正常流程"""
        with DatabaseConnection("test.db") as db:
            db.execute("SELECT * FROM users")
            db.execute("INSERT INTO users VALUES (1, 'Alice')")
            assert db.connected is True

        output = capsys.readouterr().out
        assert "连接到 test.db" in output
        assert "事务提交" in output
        assert "断开 test.db 连接" in output

    def test_queries_recorded(self):
        """SQL 被记录"""
        with DatabaseConnection("test.db") as db:
            db.execute("SELECT 1")
            db.execute("SELECT 2")
            assert db.queries == ["SELECT 1", "SELECT 2"]

    def test_exception_rollback(self, capsys):
        """异常时回滚"""
        with pytest.raises(ValueError):
            with DatabaseConnection("test.db") as db:
                db.execute("SELECT 1")
                raise ValueError("模拟错误")

        output = capsys.readouterr().out
        assert "事务回滚" in output
        assert "模拟错误" in output
        assert "断开 test.db 连接" in output

    def test_disconnected_after_exit(self):
        """退出后断开"""
        with DatabaseConnection("test.db") as db:
            pass
        assert db.connected is False

    def test_exception_not_swallowed(self):
        """异常不被吞掉"""
        with pytest.raises(RuntimeError, match="严重错误"):
            with DatabaseConnection("test.db") as db:
                raise RuntimeError("严重错误")