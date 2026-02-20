import os,ast


with open(r"C:\Users\16531\Desktop\study\daily_logs\2026-02-19.md",'r',encoding='utf-8') as file:
    # content=file.read()
    content=file.readlines()
    if os.path.exists(r"C:\Users\16531\Desktop\study\daily_logs\2026-02-20.md"):
        os.remove(r"C:\Users\16531\Desktop\study\daily_logs\2026-02-20.md")
    # print(repr(content))
    for line in content:
        every_line=repr(line)
        with open(r"C:\Users\16531\Desktop\study\daily_logs\2026-02-20.md",'a+',encoding='utf-8') as file1:
            file1.write(ast.literal_eval(every_line))