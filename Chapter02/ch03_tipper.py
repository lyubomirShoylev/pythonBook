# Tipper
#
# User enters their restaurant bill and the program
# displays two tips - a 15% and a 20% one

bill = float(input("What is your bill: "))

print(
"""
The amount you should tip were it:
\t15 percent - {0}
\t20 percent - {1}
""".format(bill * 0.15, bill * 0.20)
)

input("\nPress the enter key to exit.")