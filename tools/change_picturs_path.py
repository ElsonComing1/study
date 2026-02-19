# import os 
# import re
# import shutil


# # with open(r"../picturs/*.md")
# dirs2=os.listdir(r'C:\\Users\\16531\\Desktop\\study\\picturs')
# picturs_len=len(dirs2)
# name=input("输入你的文件名字：")        # 2026-02-19.md
# try:
#     with open(rf'daily_logs\\{name}','r+',encoding='utf-8') as file:
#         content=file.read()
#         # print(re.findall('picturs/(.*).png',content))
#         already_number=re.findall('picturs/(.*).png',content)
#         need_parse=re.findall('typora-user-images\\\\(.*).png',content)
#         # print(need_parse)
#         result=re.sub(r'\[.*\]','[]',content)
#         # print(already_number)
#         if already_number!=[]:
#             if picturs_len==int(already_number[-1]):
#                 # print('============================================')
#                 # print(picturs_len)
                
#                 # print(result)
#                 # print(content)

#                 for index,value in enumerate(need_parse):
#                     # result.replace(value,str(picturs_len+1))
#                     # print(index ,value)
#                     picturs_len+=1
#                     c=re.compile(fr'\((.*{value}.*)\)')
#                     old_name=re.search(c,result)[1]
#                     new_name=fr"C:\Users\16531\Desktop\study\picturs\{int(picturs_len)}.png"
#                     # print(new_name)
#                     os.rename(old_name,new_name)
#                     result=re.sub(rf'\(.*{value}.*\)',"(../picturs/"+str(picturs_len)+".png)",result)
#         # print(result)
#         elif already_number==[] and need_parse!=[]:
#             # print('adafase')
#             # print(f'这个{name}是全新的或者空白的')
#             for index,value in enumerate(need_parse):
#                 # result.replace(value,str(picturs_len+1))
#                 # print(index ,value)
#                 picturs_len+=1
#                 c=re.compile(fr'\((.*{value}.*)\)')
#                 old_name=re.search(c,result)[1]
#                 new_name=fr"C:\Users\16531\Desktop\study\picturs\{int(picturs_len)}.png"
#                 # print(new_name)
#                 os.rename(old_name,new_name)
#                 result=re.sub(rf'\(.*{value}.*\)',"(../picturs/"+str(picturs_len)+".png)",result)
#         else:
#             print('文件不存在！')
#         file.truncate(0)
#         file.write(result)
    

# except Exception as e:
#     print(f"当下问题是：\n{e}")

# # 
    

# dirs1=os.listdir(r'C:\\Users\\16531\\Pictures\\PixPinAutoSave')
# dirs2=os.listdir(r'C:\\Users\\16531\\AppData\\Roaming\\Typora\\typora-user-images')
# for file in dirs1:
#     os.remove('C:\\Users\\16531\\Pictures\\PixPinAutoSave\\'+file)
# for file in dirs2:
#     os.remove('C:\\Users\\16531\\AppData\\Roaming\\Typora\\typora-user-images\\'+file)




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