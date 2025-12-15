import csv
import matplotlib.pyplot as plt
date = []
pensiya = []
try: #для обработки ошибок
    with open("opendata.txt", encoding='utf-8') as ff:
        reead = csv.reader(ff)
        next(reead)
        
        for a in reead:
            if len(a) < 4:
                continue
            try:
                name, rerion, dattee, pensii = a
                if name.strip() == 'Средняя пенсия' and rerion.strip() == 'Забайкальский край' and dattee.strip().startswith('2018'):
                    date.append(dattee)
                    pensiya.append(float(pensii)) 
            except (ValueError, IndexError):
                continue
    if pensiya:
        sred = sum(pensiya) / len(pensiya)
        print(f"средняя пенсия: {sred:.2f} руб.")
    
            
 # Делаем график
        plt.figure(figsize=(10, 5))
        plt.plot(date, pensiya, 'o-', color='purple', linewidth=2)
        plt.axhline(y=sred, color='pink', linestyle='--', label=f'средняя: {sred:.2f} руб.')
        plt.title('Средняя пенсия в Забайкальском крае в 2018')
        plt.xlabel('Дата')
        plt.ylabel('Рубли')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        print("данных нет")
except FileNotFoundError:
    print("файл не найден")
except Exception as e:
    print(f" Ошибка: {e}")
