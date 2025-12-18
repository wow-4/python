import urllib.request
class Myfile:
    def __init__(self, path, mode='read'):
        self.path = path
        self.mode = mode
        self.file = None
        
           
        
#read
    def read(self):
        if self.mode != "read":
            raise ValueError('не открыт режим чтения')
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return ('файл не найден')
    
    
    
#write
    def write(self, text):
        if self.mode == 'write':
            try:
                with open(self.path, 'w', encoding='utf-8') as file:
                    file.write(text)
                    return f"запись в файл {self.path} выполнена"
            except Exception as e:
                return f"error {e}"
        else:
            raise ValueError("файл открыт не в режиме записи")
    
    
    
#append
    def write_at_the_end(self, text):
        if self.mode == 'append':
            try: 
                with open(self.path, 'a', encoding='utf-8') as file:
                    file.write(text)
                    return f"добавление в файл {self.path} выполнено"
            except Exception as e:
                return f"ошибка при добавлении в файл: {e}"
        else:
            raise ValueError("файл открыт не в режиме добавления")
        


#чтение url
    def r_url(self):      
        if self.mode != "url":
            raise ValueError("объект не в режиме URL")
        try:
            with urllib.request.urlopen(self.path) as response: #отправляет http запрос
                return response.read().decode('utf-8')#читает как байты и кодирует 
        except Exception as e:
            return f"ошибка при чтении url: {e}"
        
        
#запись url
    def w_url(self, f_name):
        if self.mode != "url":
            raise ValueError("объект не в режиме URL")
        urrl = self.r_url() 
        if not urrl.startswith("Ошибка"):
            try:
                with open(f_name, 'w', encoding='utf-8') as file:
                    file.write(urrl)
                    return f"информация записана в файл {f_name}"
            except Exception as e:
                return f"ошибка при записи: {e}"
        return urrl
    

    def __enter__(self):
        return self
    
    
    def __exit__(self, e_type, e_val, e_tb):
        if self.file:
            self.file.close()
    
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
            

file = Myfile("text.txt", "read")
text = file.read()  
print(text)

file = Myfile("text.txt", "write")
result = file.write("как дела?") 
print(result)

file = Myfile("text.txt", "append")
result = file.write_at_the_end(" how are you?")  # 
print(result)

file = Myfile("https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit", "url")
text = file.r_url() 
print(text[:400] + "...") 

result = file.w_url("textURL.txt")
print(result)

file.close()
