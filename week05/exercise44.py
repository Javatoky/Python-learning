import os
import shutil
import tempfile
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def temp_workspace(prefix: str = "workspace"):
    current_dir = Path.cwd()
    # 系统临时目录，名称唯一：tempfile.mkdtemp()创建临时目录，系统自带方法，返回路径字符串
    workspace = Path(tempfile.mkdtemp(prefix = prefix))  
    try:
        os.chdir(workspace)
        yield workspace
    finally:
        os.chdir(current_dir)
        if workspace.exists():
            shutil.rmtree(workspace)

