
class Operations:
    def __init__(self, instructions):
        
        self.opcode = []
        self.instructions = instructions.copy()
        self.const = 0
        self.registers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        print("\n------------------------------------------------------\n		    MAQUINA VIRTUAL\n------------------------------------------------------\n")
        print("Registradores: ", self.registers)


    def decode(self):
        #Analise de sintaxe e conversão para opcode
        for inst in self.instructions:
            if inst == '':
                print("Comando vazio!")
                return 1

        for inst in self.instructions:
            self.code = inst.split()

            if self.code[0] == 'SUMC':
                self.opcode.append('000')
            elif self.code[0] == 'MULC':
                self.opcode.append('001')
            elif self.code[0] == 'SUMV':
                self.opcode.append('010')
            elif self.code[0] == 'MULV':
                self.opcode.append('011')
            elif self.code[0] == 'AND':
                self.opcode.append('100')
            elif self.code[0] == 'OR':
                self.opcode.append('101')
            else:
                print("Erro de sintaxe!!\n")
                return 1

            if self.code[1] == 'VAR0':
                self.opcode.append('0000')
            elif self.code[1] == 'VAR1':
                self.opcode.append('0001')
            elif self.code[1] == 'VAR2':
                self.opcode.append('0010')
            elif self.code[1] == 'VAR3':
                self.opcode.append('0011')
            elif self.code[1] == 'VAR4':
                self.opcode.append('0100')
            elif self.code[1] == 'VAR5':
                self.opcode.append('0101')
            elif self.code[1] == 'VAR6':
                self.opcode.append('0110')
            elif self.code[1] == 'VAR7':
                self.opcode.append('0111')
            elif self.code[1] == 'VAR8':
                self.opcode.append('1000')
            else:
                print("Erro de sintaxe!!\n")
                return 1

            if self.code[2] == 'VAR0':
                self.opcode.append('0000')
            elif self.code[2] == 'VAR1':
                self.opcode.append('0001')
            elif self.code[2] == 'VAR2':
                self.opcode.append('0010')
            elif self.code[2] == 'VAR3':
                self.opcode.append('0011')
            elif self.code[2] == 'VAR4':
                self.opcode.append('0100')
            elif self.code[2] == 'VAR5':
                self.opcode.append('0101')
            elif self.code[2] == 'VAR6':
                self.opcode.append('0110')
            elif self.code[2] == 'VAR7':
                self.opcode.append('0111')
            elif self.code[2] == 'VAR8':
                self.opcode.append('1000')
            else:
                print("Erro de sintaxe!!\n")
                return 1

            if self.code[0] == 'SUMC' or self.code[0] == 'MULC':
                if int(self.code[3]) > 31:
                    self.opcode.append(f'{31:05b}')
                else:
                    self.opcode.append(f'{int(self.code[3]):05b}')
            else:
                if self.code[3] == 'VAR0':
                    self.opcode.append('00000')
                elif self.code[3] == 'VAR1':
                    self.opcode.append('00001')
                elif self.code[3] == 'VAR2':
                    self.opcode.append('00010')
                elif self.code[3] == 'VAR3':
                    self.opcode.append('00011')
                elif self.code[3] == 'VAR4':
                    self.opcode.append('00100')
                elif self.code[3] == 'VAR5':
                    self.opcode.append('00101')
                elif self.code[3] == 'VAR6':
                    self.opcode.append('00110')
                elif self.code[3] == 'VAR7':
                    self.opcode.append('00111')
                elif self.code[3] == 'VAR8':
                    self.opcode.append('01000')
                else:
                    print("Erro de sintaxe!!\n")
                    return 1
        
        print("Opcodes gerados: ")
        i=0
        for PC in range(0, len(self.opcode), 4):
            print(self.instructions[i], ":", self.opcode[PC],self.opcode[PC+1],self.opcode[PC+2],self.opcode[PC+3], "\n")
            i += 1
        return 0

    
    def execute(self, opcodeCache):
        for PC in range(0, len(opcodeCache), 4):

            #Operações
            if opcodeCache[PC] == '000':
                aux1 = int(opcodeCache[PC+1][3]) + int(opcodeCache[PC+1][2])*2 + int(opcodeCache[PC+1][1])*4 + int(opcodeCache[PC+1][0])*8
                aux2 = int(opcodeCache[PC+2][3]) + int(opcodeCache[PC+2][2])*2 + int(opcodeCache[PC+2][1])*4 + int(opcodeCache[PC+2][0])*8
                const = int(opcodeCache[PC+3][4]) + int(opcodeCache[PC+3][3])*2 + int(opcodeCache[PC+3][2])*4 + int(opcodeCache[PC+3][1])*8 + int(opcodeCache[PC+3][0])*16
                self.registers[aux1] = self.registers[aux2] + const

                #Estouro de memória
                if self.registers[aux1] > 65535:
                    self.registers[aux1] = 0
                    print("Memória excedida!")
                print("Registradores após a operação SUMC: ", self.registers)

            elif opcodeCache[PC] == '001':
                aux1 = int(opcodeCache[PC+1][3]) + int(opcodeCache[PC+1][2])*2 + int(opcodeCache[PC+1][1])*4 + int(opcodeCache[PC+1][0])*8
                aux2 = int(opcodeCache[PC+2][3]) + int(opcodeCache[PC+2][2])*2 + int(opcodeCache[PC+2][1])*4 + int(opcodeCache[PC+2][0])*8
                const = int(opcodeCache[PC+3][4]) + int(opcodeCache[PC+3][3])*2 + int(opcodeCache[PC+3][2])*4 + int(opcodeCache[PC+3][1])*8 + int(opcodeCache[PC+3][0])*16
                self.registers[aux1] = self.registers[aux2] * const

                #Estouro de memória
                if self.registers[aux1] > 65535:
                    self.registers[aux1] = 0
                    print("Memória excedida!")
                print("Registradores após a operação MULC: ", self.registers)

            elif opcodeCache[PC] == '010':
                aux1 = int(opcodeCache[PC+1][3]) + int(opcodeCache[PC+1][2])*2 + int(opcodeCache[PC+1][1])*4 + int(opcodeCache[PC+1][0])*8
                aux2 = int(opcodeCache[PC+2][3]) + int(opcodeCache[PC+2][2])*2 + int(opcodeCache[PC+2][1])*4 + int(opcodeCache[PC+2][0])*8
                aux3 = int(opcodeCache[PC+3][4]) + int(opcodeCache[PC+3][3])*2 + int(opcodeCache[PC+3][2])*4 + int(opcodeCache[PC+3][1])*8 + int(opcodeCache[PC+3][0])*16
                self.registers[aux1] = self.registers[aux2] + self.registers[aux3]

                #Estouro de memória
                if self.registers[aux1] > 65535:
                    self.registers[aux1] = 0
                    print("Memória excedida!")
                print("Registradores após a operação SUMV: ", self.registers)
                
            elif opcodeCache[PC] == '011':
                aux1 = int(opcodeCache[PC+1][3]) + int(opcodeCache[PC+1][2])*2 + int(opcodeCache[PC+1][1])*4 + int(opcodeCache[PC+1][0])*8
                aux2 = int(opcodeCache[PC+2][3]) + int(opcodeCache[PC+2][2])*2 + int(opcodeCache[PC+2][1])*4 + int(opcodeCache[PC+2][0])*8
                aux3 = int(opcodeCache[PC+3][4]) + int(opcodeCache[PC+3][3])*2 + int(opcodeCache[PC+3][2])*4 + int(opcodeCache[PC+3][1])*8 + int(opcodeCache[PC+3][0])*16
                self.registers[aux1] = self.registers[aux2] * self.registers[aux3]

                #Estouro de memória
                if self.registers[aux1] > 65535:
                    self.registers[aux1] = 0
                    print("Memória excedida!")
                print("Registradores após a operação MULV: ", self.registers)

            elif opcodeCache[PC] == '100':
                aux1 = int(opcodeCache[PC+1][3]) + int(opcodeCache[PC+1][2])*2 + int(opcodeCache[PC+1][1])*4 + int(opcodeCache[PC+1][0])*8
                aux2 = int(opcodeCache[PC+2][3]) + int(opcodeCache[PC+2][2])*2 + int(opcodeCache[PC+2][1])*4 + int(opcodeCache[PC+2][0])*8
                aux3 = int(opcodeCache[PC+3][4]) + int(opcodeCache[PC+3][3])*2 + int(opcodeCache[PC+3][2])*4 + int(opcodeCache[PC+3][1])*8 + int(opcodeCache[PC+3][0])*16

                print("Executando operação lógica...")
                print(f'{self.registers[aux2]:05b}', "AND", f'{self.registers[aux3]:05b}')
                resp = self.registers[aux2] & self.registers[aux3]
                self.registers[aux1] = resp
                print("Registradores após a operação AND: ", self.registers, '\n')
            
            elif opcodeCache[PC] == '101':
                aux1 = int(opcodeCache[PC+1][3]) + int(opcodeCache[PC+1][2])*2 + int(opcodeCache[PC+1][1])*4 + int(opcodeCache[PC+1][0])*8
                aux2 = int(opcodeCache[PC+2][3]) + int(opcodeCache[PC+2][2])*2 + int(opcodeCache[PC+2][1])*4 + int(opcodeCache[PC+2][0])*8
                aux3 = int(opcodeCache[PC+3][4]) + int(opcodeCache[PC+3][3])*2 + int(opcodeCache[PC+3][2])*4 + int(opcodeCache[PC+3][1])*8 + int(opcodeCache[PC+3][0])*16

                print("Executando operação lógica...")
                print(f'{self.registers[aux2]:05b}', "OR", f'{self.registers[aux3]:05b}')
                resp = self.registers[aux2] | self.registers[aux3]
                self.registers[aux1] = resp
                print("Registradores após a operação OR: ", self.registers, '\n')

        print("Execução finalizada...")
        print("Cache Miss...\n")

    def cache(self):
        cacheList = [[False, []], [False, []], [False, []], [False, []]]
        

        print("Cache Miss...")
        for inst in range(0, len(self.opcode), 16):
            
            if len(self.opcode) - inst >= 16:
                cacheList[0][0] = True
                cacheList[0][1] = self.opcode[inst:inst+4].copy()
                cacheList[1][0] = True
                cacheList[1][1] = self.opcode[inst+4:inst+8].copy()
                cacheList[2][0] = True
                cacheList[2][1] = self.opcode[inst+8:inst+12].copy()
                cacheList[3][0] = True
                cacheList[3][1] = self.opcode[inst+12:inst+16].copy()

            elif len(self.opcode) - inst == 12:
                cacheList[0][0] = True
                cacheList[0][1] = self.opcode[inst:inst+4].copy()
                cacheList[1][0] = True
                cacheList[1][1] = self.opcode[inst+4:inst+8].copy()
                cacheList[2][0] = True
                cacheList[2][1] = self.opcode[inst+8:inst+12].copy()

            elif len(self.opcode) - inst == 8:
                cacheList[0][0] = True
                cacheList[0][1] = self.opcode[inst:inst+4]
                cacheList[1][0] = True
                cacheList[1][1] = self.opcode[inst+4:inst+8]

            elif len(self.opcode) - inst == 4:
                cacheList[0][0] = True
                cacheList[0][1] = self.opcode[inst:inst+4]
            
            opcodeCache = []
            if cacheList[0][0]:
                opcodeCache += cacheList[0][1]
            if cacheList[1][0]:
                opcodeCache += cacheList[1][1]
            if cacheList[2][0]:
                opcodeCache += cacheList[2][1]
            if cacheList[3][0]:
                opcodeCache += cacheList[3][1]

            print("Cache Hit...")
            self.execute(opcodeCache)

            if cacheList[0][0]:
                cacheList[0][0] = False

            if cacheList[1][0]:
                cacheList[1][0] = False
                
            if cacheList[2][1]:
                cacheList[2][0] = False

            if cacheList[3][0]:
                cacheList[3][0] = False
            

