import tkinter as tk
import pandas as pd

def increase_value(value):
    value.set(value.get() + 1)

def decrease_value(value):
    value.set(value.get() - 1)

def reset_values(strength, charisma, agility, intelligence):
    strength.set(0)
    charisma.set(0)
    agility.set(0)
    intelligence.set(0)

def save_values_to_excel(strength, charisma, agility, intelligence):
    df = pd.DataFrame({"Strength": [strength.get()],
                       "Charisma": [charisma.get()],
                       "Agility": [agility.get()],
                       "Intelligence": [intelligence.get()]})
    df.to_excel(r"C:\Users\laith\OneDrive\Desktop\Stuff\excel_python_folder\character_stats.xlsx", index=False)

root = tk.Tk()
root.title("Character Stats")

strength = tk.IntVar()
charisma = tk.IntVar()
agility = tk.IntVar()
intelligence = tk.IntVar()

try:
    df = pd.read_excel(r"C:\Users\laith\OneDrive\Desktop\Stuff\excel_python_folder\character_stats.xlsx")
    strength.set(df["Strength"].iloc[0])
    charisma.set(df["Charisma"].iloc[0])
    agility.set(df["Agility"].iloc[0])
    intelligence.set(df["Intelligence"].iloc[0])
except FileNotFoundError:
    pass

strength_label = tk.Label(root, text="Strength:")
strength_label.grid(row=0, column=0)
strength_value_label = tk.Label(root, textvariable=strength)
strength_value_label.grid(row=0, column=1)
strength_increase_button = tk.Button(root, text="+", command=lambda: increase_value(strength))
strength_increase_button.grid(row=0, column=3)
strength_decrease_button = tk.Button(root, text="-", command=lambda: decrease_value(strength))
strength_decrease_button.grid(row=0, column=2)

charisma_label = tk.Label(root, text="Charisma:")
charisma_label.grid(row=1, column=0)
charisma_value_label = tk.Label(root, textvariable=charisma)
charisma_value_label.grid(row=1, column=1)
charisma_increase_button = tk.Button(root, text="+", command=lambda: increase_value(charisma))
charisma_increase_button.grid(row=1, column=3)
charisma_decrease_button = tk.Button(root, text="-", command=lambda: decrease_value(charisma))
charisma_decrease_button.grid(row=1, column=2)

agility_label = tk.Label(root, text="Agility:")
agility_label.grid(row=2, column=0)
agility_value_label = tk.Label(root, textvariable=agility)
agility_value_label.grid(row=2, column=1)
agility_increase_button = tk.Button(root, text="+", command=lambda: increase_value(agility))
agility_increase_button.grid(row=2, column=3)
agility_decrease_button = tk.Button(root, text="-", command=lambda: decrease_value(agility))
agility_decrease_button.grid(row=2, column=2)

intelligence_label = tk.Label(root, text="Intelligence:")
intelligence_label.grid(row=3, column=0)
intelligence_value_label = tk.Label(root, textvariable=intelligence)
intelligence_value_label.grid(row=3, column=1)
intelligence_increase_button = tk.Button(root, text="+", command=lambda: increase_value(intelligence))
intelligence_increase_button.grid(row=3, column=3)
intelligence_decrease_button = tk.Button(root, text="-", command=lambda: decrease_value(intelligence))
intelligence_decrease_button.grid(row=3, column=2)

save_button = tk.Button(root, text="Save", width=20, command=lambda: save_values_to_excel(strength, charisma, agility, intelligence))
save_button.grid(row=4, column=0, columnspan=4, sticky="we")

reset_button = tk.Button(root, text="Reset", width=20, command=lambda: reset_values(strength, charisma, agility, intelligence))
reset_button.grid(row=5, column=0, columnspan=5, sticky="we")

root.mainloop()