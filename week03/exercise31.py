def safe_convert(value: str, target_type: type, default=None):
    try:
        new_value = target_type(value)
    except ValueError:
        return default
    else:
        return new_value
print(safe_convert("42", int))           
print(safe_convert("3.14", float))       
print(safe_convert("abc", int))         
print(safe_convert("abc", int, 0))

def safe_get(data: dict, *keys, default=None):
    value = data
    for key in keys:
        try:
            value = value[key]
        except KeyError:
            return default
    return value
data = {"user": {"name": "Alice", "address": {"city": "Beijing"}}}
print(safe_get(data, "user", "name"))
print(safe_get(data, "user", "address", "city"))
print(safe_get(data, "user", "phone"))
print(safe_get(data, "x", "y", default="N/A"))

def read_file_safe(filepath: str) -> str:
    try:
        with open(filepath, "r") as f:
            content = f.read()      # json.load()是读取JSON文件，读取文本文件用File.read()
    except FileNotFoundError as e:
        print(f"文件不存在！")
        content = ''
        return content
    except PermissionError as e:
        print(f'没有访问权限')
        content = ''
        return content
    except UnicodeDecodeError as e:
        with open(filepath, "r", encoding = 'utf-8', errors = "replace") as f:
            content = f.read()
            return content
#    finally:
#        return content     finally语句会强制最后执行，无论前面异常是否捕获和抛出，都会执行finally块的代码，所以不要在finally中return，里面只能做检查和关闭资源