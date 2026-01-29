import nbtlib
import ast

data = nbtlib.load('player.dat')
nbt_str = str(data.snbt())  # Преобразуем в строку SNBT
python_dict = ast.literal_eval(nbt_str)  # Преобразуем в dict
print(python_dict)