"""
The program can be ran through main with `python code` command in your terminal,
or through each file individually.·..·@ſeæßð«»¢æßð@ſßßßææ«««»»¢¢ððee¶¶đ„„ŋ¶ŧŋ““”ħ←ŧ↓ˀ”“”µħˀĸłˀĸ↓→øŧ←↓
"""

options = [
    "Generate Feigenbaum's constant",
    "Obtain max value",
    "Lyapunov multiprocessing",
    "Cobweb plot",
    "Fourier plot",
    "Transitivity",
]

for i, option in enumerate(options, start=1):
    print(f"[{i}] {option}")

while True:
    try:
        choice = float(input("Please select the program you would like to run: "))
        if 1 <= choice <= 6:
            break
        else:
            print("Invalid input, please try again.")
    except ValueError:
        print("Invalid input, please try selecting a number.")

if choice == 1:
    feigenbaum()
elif choice == 2:
    lyapunov()
else:
    print("Choice value error")
