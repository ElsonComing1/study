import os,ast,re



def read_file(filename):
    with open(rf"{filename}",'r',encoding='utf-8') as file:
        content=file.read()
        file.close()
    return content


def readlines_file(filename):
    with open(rf"{filename}",'r',encoding='utf-8') as file:
        content=file.readlines()
        file.close()
    return content


def writelines_file(filename,line):
    with open(rf"{filename}",'a+',encoding='utf-8') as file:
        file.write(line)
    file.close()
    
def exists_delete(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def tr_prictur_path(line):
    global last_num
    # print(last_num)
    line=repr(line)
    # print(line)
    complie_text=re.compile(r'typora-user-images\\\\(\d+\.png)')
    pictur_file_name=re.search(complie_text,line)
    if pictur_file_name!=None:
        pictur_file_name=pictur_file_name[1]
        # print(pictur_file_name[1])
        base_picturs=os.listdir(pictur_base_path)
        if pictur_file_name in base_picturs:
            picture_path=pictur_base_path+pictur_file_name
            last_num+=1
            new_pictur_name=str(last_num)+".png"
            new_picture_path=destetion_pictur_path+new_pictur_name
            # print(new_pictur_name)


            os.rename(picture_path,new_picture_path)

            line1=re.sub(r'(\[\d+\])',"[]",line)
            line2=re.sub(r'\(.+\)',f'(../picturs/{new_pictur_name})',line1)
            # print(line2)
            writelines_file(tmp_file_path,ast.literal_eval(line2))
    


    else:
        line=ast.literal_eval(line)
        writelines_file(tmp_file_path,line)
    
def remove_file(dir_path):
    files=os.listdir(dir_path)
    if len(files)!=0:
        for file in files:
            if os.path.exists(f"{dir_path+file}"):
                os.remove(f"{dir_path+file}")

# print(len(already_num))
if __name__=="__main__":
    destetion_pictur_path=r"C:\Users\16531\Desktop\study\picturs\\"
    pictur_base_path=r"C:\\Users\\16531\\AppData\\Roaming\\Typora\\typora-user-images\\"
    text_name_path=r"C:\Users\16531\Desktop\study\daily_logs\2026-02-20.md"
    tmp_file_path=r"C:\Users\16531\Desktop\study\daily_logs\new.md"


    content=read_file(text_name_path)
    already_num=re.findall(r'picturs/(\d+)\.png',content)
    exists_delete(tmp_file_path)


    if len(already_num)!=0:
        last_num=int(already_num[-1])
        lines=readlines_file(text_name_path)
        for line in lines:
            tr_prictur_path(line)
        # print(last_num)

    elif len(already_num)==0:
        last_num=int(str(os.listdir(destetion_pictur_path)[-1]).split('.')[0])
        lines=readlines_file(text_name_path)
        for line in lines:
            tr_prictur_path(line)

    else:
        print('no')
    os.remove(text_name_path)
    os.rename(tmp_file_path,text_name_path)
    remove_file(r"C:\Users\16531\AppData\Roaming\Typora\typora-user-images")
    remove_file(r"C:\Users\16531\Pictures\PixPinAutoSave")