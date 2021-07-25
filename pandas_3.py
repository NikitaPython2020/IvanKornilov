import pandas as pd
import matplotlib.pyplot as plt

def heighGroup(row):
    if row['Height (m)'] <= 7500:
        return 'High'
    if row['Height (m)'] <= 8000:
        return 'Very High'
    if row['Height (m)'] > 8000:
        return 'Extrimely High'

mountains = pd.read_csv('C:/Users/user/Desktop/Нетология/01. Подготовка/ds3-spring-2018/0. Preparatory week/0.2 Python for DS/Homework/mountains.csv', sep=',')

mountains['mountHigh'] = mountains.apply(heighGroup, axis=1)
print(mountains['mountHigh'].value_counts())

mountains.to_csv('C:/Users/user/Desktop/Нетология/01. Подготовка/ds3-spring-2018/0. Preparatory week/0.2 Python for DS/Homework/mount_modif.csv', sep=';', na_rep='0', columns=['Rank','Mountain','Height (m)','mountHigh'],index=False)

mountains.to_json('C:/Users/user/Desktop/Нетология/01. Подготовка/ds3-spring-2018/0. Preparatory week/0.2 Python for DS/Homework/mount_modif.json')

mountains.to_excel('C:/Users/user/Desktop/Нетология/01. Подготовка/ds3-spring-2018/0. Preparatory week/0.2 Python for DS/Homework/mount_modif.xlsx', sheet_name='mounts')

#print(mountains.describe())
#print(mountains['First ascent'].value_counts()[0])
#print(mountains['First ascent'].value_counts().index[0], mountains['First ascent'].value_counts()[0])
#print(mountains['First ascent'].value_counts().sort_index())
#print(mountains['First ascent'].value_counts())
#mountains['First ascent'].hist(bins=100, figsize=(30,5))

# plt.show()