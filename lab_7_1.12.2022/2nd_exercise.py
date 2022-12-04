class ContainsVirusError(Exception):
    pass
try:
    file = open("Something.txt", "r")

except FileNotFoundError:
    print("File not found.")
except OSError:
    print("You dont have permission to open this file!")
except ContainsVirusError:
    print("The file can't be opened due to virus.")
else:
    file.close()

