# Data Retrival
import os

Contact_Book = []

def get_data():
    if os.path.exists("app_data.csv") == False:
        return
    else:
        with open("app_data.csv") as data_file:
            for line in data_file:
                # [name, phonenum, address, longitude, latitude]
                data_list = line.strip().split(",")
                Contact_Book.append(data_list)
        data_file.close()

def store_data():
    if os.path.exists("app_data.csv") == False:
        return
    else:
        file = open("app_data.csv", "a")
        file.write("\nsample, sample, sample, sample, sample")
        file.close()
