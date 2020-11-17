import fileinput

#funca funca
with fileinput.FileInput('/home/jonimottg/Escritorio/Memoria/Freya/catalogs/ztf/methods.py', inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('NAME', f'{catalog}'), end='')