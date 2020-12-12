from modules import operations

if __name__ == "__main__":
    while True:
        print("\n------------------------------------------------------\n		    MAQUINA VIRTUAL\n------------------------------------------------------\n")
        comand = ""
        comands = []
        while comand != "EXECUTE":
            comand = input('Insira os comandos: \n')
            comand = comand.upper()
            if comand == 'EXIT':
                break
            comands.append(comand)
            
        if comand != 'EXIT':
            comands.pop()
            operation = operations.Operations(comands)
            if operation.decode() == 0:
                operation.cache()
        else:
            break
