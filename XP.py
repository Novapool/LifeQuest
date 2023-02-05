import tkinter as tk


def calculate_xp(strength, agility, intelligence, charisma, level, base_xp=10):
    a, b, c, d = 1, 1, 1, 1
    xp = a * strength + b * agility + c * intelligence + d * charisma
    xp_required = base_xp * (1.5) ** (level - 1)
    return xp, xp_required

strength, agility, intelligence, charisma =1, 5, 0, 0
level = 3
xp, xp_required = calculate_xp(strength, agility, intelligence, charisma, level)

if xp >= xp_required:
    level += 1
    print(f"Congratulations, you have reached level {level} with {xp} XP!")
else:
    print(f"You need {xp_required - xp} more XP to reach level {level + 1}.")

root = tk.Tk()
root.title("XP")

label = tk.Label(root, text="You level is: " + str(level))
label.pack()
label2 = tk.Label(root, text="Your xp is: " + str(xp) + '/' + str((round)(xp_required)))
label2.pack()






root.mainloop()

