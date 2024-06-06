import streamlit as st
import matplotlib.pyplot as plt


def get_ages(inner_file, stat, sex):
    inner_file = iter(inner_file)
    lst = []
    next(inner_file)
    for line in inner_file:
        line = line.split(',')
        if bool(int(line[1])) != stat:
            continue
        if line[5] == sex:
            if line[6] == '':
                lst.append(0)
            else:
                lst.append(float(line[6]))

    return lst


filename = 'data.csv'

# Создание сайта с изображением Титаника и диаграммой
st.title('Титаник: статистика пассажиров')
st.image('t.jpg', use_column_width=True)

status = st.radio('Выберите статус пассажира:', ('Спасен', 'Погиб'))
gender = st.radio('Выберите пол пассажира:', ('Мужчины', 'Женщины'))

fig, ax = plt.subplots()
my_dict = {
    'Мужчины': 'male',
    'Женщины': 'female',
}

with open(filename, 'r') as file:
    if status == 'Спасен':
        passengers = get_ages(file, True, my_dict[gender])
        st.write(f'Минимальный возраст спасенных {gender.lower()[:-1]}: {min(passengers)}')
        st.write(f'Максимальный возраст спасенных {gender.lower()[:-1]}: {max(passengers)}')

    else:
        passengers = get_ages(file, False, my_dict[gender])
        st.write(f'Минимальный возраст погибших {gender.lower()[:-1]}: {min(passengers)}')
        st.write(f'Максимальный возраст погибших {gender.lower()[:-1]}: {max(passengers)}')

# Создание диаграммы

ax.hist(passengers, bins=10, alpha=0.5, label=gender)
plt.xlabel('Возраст')
plt.ylabel('Количество')
plt.legend()
st.pyplot(fig)