raw_config = """
# 数据库配置
db_host = localhost
db_port = 5432
db_name = myapp

# 服务器配置
server_port = 8080
debug = true
max_connections = 100

# 以下是故意放的"脏数据"
bad_line_no_equals
empty_value = 
port_wrong_type = abc
negative_number = -1
"""

class ConfigError(Exception):
    """配置异常"""
    pass

class ParseError(ConfigError):
    def __init__(self, line_count, line_content):
        self.line_count = line_count
        self.line_content = line_content
        super().__init__(f'解析失败，第{line_count}行内容有误：{line_content}(忽略注释和空行)')

class ValidationError(ConfigError):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        super().__init__(f'值验证失败：{key} = {value}')

import re


def parse_config(raw: str) -> dict:
    # """跳过空行和 # 开头的注释行"""
    # first_process = re.sub(r'\n\n', '\n', raw_config)
    # second_process = re.sub(r'\n# [\w."]+\n', '\n', first_process)
    # third_process = second_process.strip()

    # 这个正则只能匹配特定格式的注释（如 # 数据库配置），如果注释内容变了就失效了。更简单的方式：逐行处理，遇到 # 开头或空行就跳过（为什么当时我就想不到）
    config_dict = {}
    for i,line in enumerate(raw.strip().splitlines(), start = 1):
        """跳过空行和 # 开头的注释行"""
        if not line or line.startswith('#'):
            continue
        """按 = 分割键值对，去除空格"""
        if '=' not in line:
            print(ParseError(i, line))
            continue
        # key_and_value = line.split('=')
        # key = key_and_value[0].strip()
        # value = key_and_value[1].strip()
        key, _, value = line.partition("=")     # partition 只分一次，比 split 更安全
        # 新知识：str.partition(sep) 返回 (前, 分隔符, 后) 三元组，**只按第一个 = 分割**。**比 split("=") 更安全**（如果值中包含 = 不会出错）。
        key = key.strip()
        value = value.strip()
        if value == '':
            value = None
        elif value == 'true' or value == 'false':
            value = (value == 'true')
        # elif all(element in "1234567890\n" for element in value.replace('-', '\n')):
            # value = int(value)
        # 上面的逻辑有点绕，直接从Python的EAFP原则思考，先尝试转，转不了过
        try:
            value = int(value)
        except (ValueError, TypeError):
            pass
        config_dict[key] = value
    return config_dict
    

def validate_config(config: dict) -> list[str]:
    errors_list = []
    for key, value in config.items():
        value_type = type(value)
        # if value == None:     错误！
        # 判断是否是None用 is
        if value is None:
            e = ValidationError(key, value)
            errors_list.append(e)
            continue
        if "port" in key and not value_type is int:
            e = ValidationError(key, value)
            errors_list.append(e)
            continue
        if value_type is int and value < 0:
            e = ValidationError(key, value)
            errors_list.append(e)
    return errors_list
        
                
if __name__ == '__main__':
    config = parse_config(raw_config)
    errors_list = validate_config(config)
    for error in errors_list:
        print(error)