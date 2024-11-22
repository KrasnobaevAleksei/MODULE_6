import inspect
import sys

def introspection_info(obj):
        res = {}
        methods = []
        attribute = []
        for i in dir(42):
            if i.endswith("__"):
                methods.append(i)
            else:
                attribute.append(i)
        res['type'] = (type(obj))#тип
        res['attributes'] = attribute
        res['methods'] = methods
        res['module'] = (inspect.getmodule(obj))  # модуль

        return res

if __name__ == "__main__":
    num_ = 42
    number_info = introspection_info(num_)
    print(number_info)
    print(sys.builtin_module_names)

