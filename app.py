import os, time

BASE_DIR = os.getcwd()

no_read = ['.git', 'app.py', '__pycache__',]

name = str(input("Enter name to rename: "))
number = int(input("Enter the number at which the count starts: "))
ext = str(input("Enter the extension: "))

print('\nIniciando o processo de renomar os arquivos...')
time.sleep(2)
for filename in os.listdir(BASE_DIR):
    if filename not in no_read:
        cont_name = "{}_{}.{}".format(name, number, ext)

        print("\nRenomeando: ", filename)
        os.rename(filename, cont_name)
        print("Para: ", cont_name)

        number+=1
print('\nFinalizado')

