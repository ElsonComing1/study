import os
import re
import shutil

# 配置路径
BASE_DIR = r'C:\Users\16531\Desktop\study'
PICTURS_DIR = os.path.join(BASE_DIR, 'picturs')
DAILY_LOGS_DIR = os.path.join(BASE_DIR, 'daily_logs')

dirs2 = os.listdir(PICTURS_DIR)
picturs_len = len(dirs2)
name = input("输入你的文件名字：")  # 2026-02-19.md

try:
    file_path = os.path.join(DAILY_LOGS_DIR, name)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    already_number = re.findall(r'picturs/(\d+)\.png', content)
    need_parse = re.findall(r'typora-user-images\\([^\\]+)\.png', content)
    
    # 关键修复：不要替换方括号，直接操作原内容
    result = content  # 保留原格式，包括换行符
    
    if already_number:
        last_number = max([int(n) for n in already_number])
    else:
        last_number = 0
    
    if need_parse:
        for value in need_parse:
            picturs_len += 1
            # 匹配旧路径（支持括号内任意字符）
            pattern = rf'\(([^)]*{re.escape(value)}[^)]*)\)'
            match = re.search(pattern, result)
            
            if match:
                old_name = match.group(1)
                new_name = os.path.join(PICTURS_DIR, f"{picturs_len}.png")
                
                # 重命名文件
                if os.path.exists(old_name):
                    os.rename(old_name, new_name)
                
                # 替换路径（保留方括号和换行格式）
                new_path = f"(../picturs/{picturs_len}.png)"
                result = result.replace(match.group(0), new_path)
        
        # 写回文件（使用 'w' 模式，不需要 truncate）
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(result)
        print(f"处理完成，共处理 {len(need_parse)} 张图片")
    else:
        print('没有需要处理的图片')
        
except Exception as e:
    print(f"当下问题是：\n{e}")
    import traceback
    traceback.print_exc()

# 清理临时文件
dirs1 = os.listdir(r'C:\Users\16531\Pictures\PixPinAutoSave')
dirs3 = os.listdir(r'C:\Users\16531\AppData\Roaming\Typora\typora-user-images')

for file in dirs1:
    try:
        os.remove(os.path.join(r'C:\Users\16531\Pictures\PixPinAutoSave', file))
    except:
        pass
        
for file in dirs3:
    try:
        os.remove(os.path.join(r'C:\Users\16531\AppData\Roaming\Typora\typora-user-images', file))
    except:
        pass