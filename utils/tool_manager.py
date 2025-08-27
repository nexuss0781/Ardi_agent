import importlib
import os

class ToolManager:
    def __init__(self):
        self.tools = {}
        self._load_tools()

    def _load_tools(self):
        tools_dir = "tools"
        for filename in os.listdir(tools_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]  # Remove .py extension
                module_path = f"{tools_dir}.{module_name}"
                try:
                    module = importlib.import_module(module_path)
                    for item_name in dir(module):
                        item = getattr(module, item_name)
                        if isinstance(item, type) and hasattr(item, '__init__') and item.__module__ == module.__name__:
                            # Assuming tools are classes that can be instantiated without args for now
                            # This needs to be more robust for tools with specific init requirements
                            self.tools[item_name] = item()
                            print(f"Loaded tool: {item_name}")
                except Exception as e:
                    print(f"Error loading tool {module_name}: {e}")

    def get_tool(self, tool_name: str):
        return self.tools.get(tool_name)

    def list_tools(self):
        return list(self.tools.keys())

    def execute_tool(self, tool_name: str, method_name: str, *args, **kwargs):
        tool = self.get_tool(tool_name)
        if tool:
            if hasattr(tool, method_name) and callable(getattr(tool, method_name)):
                method = getattr(tool, method_name)
                try:
                    return method(*args, **kwargs)
                except Exception as e:
                    print(f"Error executing tool {tool_name}.{method_name}: {e}")
                    return None
            else:
                print(f"Method {method_name} not found in tool {tool_name}")
                return None
        else:
            print(f"Tool {tool_name} not found")
            return None


