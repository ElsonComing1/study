import os 
import re
import shutil


# with open(r"../picturs/*.md")
dirs2=os.listdir(r'C:\\Users\\16531\\Desktop\\study\\picturs')
picturs_len=len(dirs2)
name=input("输入你的文件名字：")        # 2026-02-19.md
try:
    with open(rf'daily_logs\\{name}','r+',encoding='utf-8') as file:
        content=file.read()
        # print(re.findall('picturs/(.*).png',content))
        already_number=re.findall('picturs/(.*).png',content)
        need_parse=re.findall('typora-user-images\\\\(.*).png',content)
        # print(need_parse)
        result=re.sub(r'\[.*\]','[]',content)
        # print(already_number)
        if already_number!=[]:
            if picturs_len==int(already_number[-1]):
                # print('============================================')
                # print(picturs_len)
                
                # print(result)
                # print(content)

                for index,value in enumerate(need_parse):
                    # result.replace(value,str(picturs_len+1))
                    # print(index ,value)
                    picturs_len+=1
                    c=re.compile(fr'\((.*{value}.*)\)')
                    old_name=re.search(c,result)[1]
                    new_name=fr"C:\Users\16531\Desktop\study\picturs\{int(picturs_len)}.png"
                    # print(new_name)
                    os.rename(old_name,new_name)
                    result=re.sub(rf'\(.*{value}.*\)',"(../picturs/"+str(picturs_len)+".png)",result)
        # print(result)
        elif already_number==[] and need_parse!=[]:
            # print('adafase')
            # print(f'这个{name}是全新的或者空白的')
            for index,value in enumerate(need_parse):
                # result.replace(value,str(picturs_len+1))
                # print(index ,value)
                picturs_len+=1
                c=re.compile(fr'\((.*{value}.*)\)')
                old_name=re.search(c,result)[1]
                new_name=fr"C:\Users\16531\Desktop\study\picturs\{int(picturs_len)}.png"
                # print(new_name)
                os.rename(old_name,new_name)
                result=re.sub(rf'\(.*{value}.*\)',"(../picturs/"+str(picturs_len)+".png)",result)
        else:
            print('文件不存在！')
        file.truncate(0)
        file.write(result)
    

except Exception as e:
    print(f"当下问题是：\n{e}")


    

dirs1=os.listdir(r'C:\\Users\\16531\\Pictures\\PixPinAutoSave')
dirs2=os.listdir(r'C:\\Users\\16531\\AppData\\Roaming\\Typora\\typora-user-images')
for file in dirs1:
    os.remove('C:\\Users\\16531\\Pictures\\PixPinAutoSave\\'+file)
for file in dirs2:
    os.remove('C:\\Users\\16531\\AppData\\Roaming\\Typora\\typora-user-images\\'+file)


