#built in shell tool
from langchain_community.tools import ShellTool

shell_tool = ShellTool()
results  = shell_tool.invoke('whoami')
print(results)