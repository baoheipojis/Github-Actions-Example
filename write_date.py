# write_date.py
import datetime

def write_date_to_file():
    # 获取当前日期
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 将当前日期写入文件
    with open("date_log.txt", "a") as file:
        file.write(f"{current_date}\n")

if __name__ == "__main__":
    write_date_to_file()