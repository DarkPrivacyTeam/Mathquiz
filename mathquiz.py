import time
import random 

banner1 = '''
 .S_SsS_S.    .S_SSSs    sdSS_SSSSSSbs   .S    S.   
.SS~S*S~SS.  .SS~SSSSS   YSSS~S%SSSSSP  .SS    SS.  
S%S `Y' S%S  S%S   SSSS       S%S       S%S    S%S  
S%S     S%S  S%S    S%S       S%S       S%S    S%S  
S%S     S%S  S%S SSSS%S       S&S       S%S SSSS%S  
S&S     S&S  S&S  SSS%S       S&S       S&S  SSS&S  
S&S     S&S  S&S    S&S       S&S       S&S    S&S  
S&S     S&S  S&S    S&S       S&S       S&S    S&S  
S*S     S*S  S*S    S&S       S*S       S*S    S*S  
S*S     S*S  S*S    S*S       S*S       S*S    S*S  
S*S     S*S  S*S    S*S       S*S       S*S    S*S  
SSS     S*S  SSS    S*S       S*S       SSS    S*S  
        SP          SP        SP               SP   
        Y           Y         Y                Y    
                                                    
  sSSs_sSSs     .S       S.    .S   sdSSSSSSSbs     
 d%%SP~YS%%b   .SS       SS.  .SS   YSSSSSSSS%S     
d%S'     `S%b  S%S       S%S  S%S          S%S      
S%S       S%S  S%S       S%S  S%S         S&S       
S&S       S&S  S&S       S&S  S&S        S&S        
S&S       S&S  S&S       S&S  S&S        S&S        
S&S       S&S  S&S       S&S  S&S       S&S         
S&S       S&S  S&S       S&S  S&S      S*S          
S*b       d*S  S*b       d*S  S*S     S*S           
S*S.     .S*S  S*S.     .S*S  S*S   .s*S            
 SSSbs_sdSSSS   SSSbs_sdSSS   S*S   sY*SSSSSSSP     
  YSSP~YSSSSS    YSSP~YSSY    S*S  sY*SSSSSSSSP     
                              SP                    
                              Y                     
                                                 
'''
print(banner1)
print("Oi, meu nome e n00b criador do jogo game of n00b v1.kill, E criador desse jogo tambem, e caso tenha algum problema no jogo mande para esse numero: 8791075168.")
print("\n\nAGORA VAMOS COMEÇA!!!!")
time.sleep(1)
print("\n\n-[1] -> Multiplicaçao")
print("-[2] -> divisao")
print("-[3] -> subtraçao")
print("-[4] -> adiçao")
print("-[5] -> raiz quadrada")

op = int(input("\ndigite qual quiz voce quer faze ->" ))

win = 0
erro = 0
rep = 0
vol = 0

if op == 1:
	while (rep != 2):
		vol += 1
		mul1 = random.randint(0, 10)
		mul2 = random.randint(0, 10)
		multiR = mul1*mul2
		numM = int(input(f"qual e o resultado de {mul1}x{mul2}? ->"))
		if numM == multiR:
			print("\nParabens!!, voce acertou")
			win += 0
			if vol == 10:
				rep = int(input("\ndeseja continua?, se sim digite |1|-> "))
				print(f"acertos: {win} erros: {erro} rodadas: {vol}")
		elif numM != multiR:
			erro += 1
			print("Aaaa..., nao foi dessa!!!, tente novamente")
			if vol == 10:
				rep = int(input("\ndeseja continua?, se sim digite |1|-> "))
				print(f"acertos: {win} erros: {erro} rodadas: {vol}")
			if rep == 2:
				break
elif op == 4:
	while (rep != 2):
		vol += 1
		add1 = random.randint(0, 100)
		add2 = random.randint(0, 100)
		addR = add1+add2
		numM = int(input(f"qual e o resultado de {add1}+{add2}? ->"))
		if numM == addR:
			print("\nParabens!!, voce acertou")
			win += 0
			if vol == 10:
				rep = int(input("\ndeseja continua?, se sim digite |1|-> "))
				print(f"acertos: {win} erros: {erro} rodadas: {vol}")
		elif numM != addR:
			erro += 1
			print("Aaaa..., nao foi dessa!!!, tente novamente")
			if vol == 10:
				rep = int(input("\ndeseja continua?, se sim digite |1|-> "))
				print(f"acertos: {win} erros: {erro} rodadas: {vol}")
			if rep == 2:
				break
elif op == 3:
	while (rep != 2):
		vol += 1
		sub1 = random.randint(0, 200)
		sub2 = random.randint(0, 200)
		subR = sub1-sub2
		numM = int(input(f"qual e o resultado de {sub1}-{sub2}? ->"))
		if numM == subR:
			print("\nParabens!!, voce acertou")
			win += 0
			if vol == 10:
				rep = int(input("\ndeseja continua?, se sim digite |1|-> "))
				print(f"acertos: {win} erros: {erro} rodadas: {vol}")
		elif numM != subR:
			erro += 1
			print("Aaaa..., nao foi dessa!!!, tente novamente")
			if vol == 10:
				rep = int(input("\ndeseja continua?, se sim digite |1|-> "))
				print(f"acertos: {win} erros: {erro} rodadas: {vol}")
			if rep == 2:
				break
elif op == 5:
	while (rep != 2):
		vol += 1
		raiz1 = random.randint(0, 10)
		raiz2= random.randint(0, 10)
		raizR = raiz1**raiz2
		numM = int(input(f"qual e o resultado de {raiz1}√{raiz2}? ->"))
		if numM == raizR:
			print("\nParabens!!, voce acertou")
			win += 0
			if vol == 10:
				rep = int(input("\ndeseja continua?, se sim digite |1|-> "))
				print(f"acertos: {win} erros: {erro} rodadas: {vol}")
		elif numM != raizR:
			erro += 1
			print("Aaaa..., nao foi dessa!!!, tente novamente")
			if vol == 10:
				rep = int(input("\ndeseja continua?, se sim digite |1|-> "))
				print(f"acertos: {win} erros: {erro} rodadas: {vol}")
			if rep == 2:
				break
elif op == 2:
	while (rep != 2):
		vol += 1
		div1 = random.randint(0, 100)
		div2 = random.randint(0, 100)
		divR = div1*div2
		numM = int(input(f"qual e o resultado de {div1}÷{div2}? ->"))
		if numM == divR:
			print("\nParabens!!, voce acertou")
			win += 0
			if vol == 10:
				rep = int(input("\ndeseja continua?, se sim digite |1|-> "))
				print(f"acertos: {win} erros: {erro} rodadas: {vol}")
		elif numM != divR:
			erro += 1
			print("Aaaa..., nao foi dessa!!!, tente novamente")
			if vol == 10:
				rep = int(input("\ndeseja continua?, se sim digite |1|-> "))
				print(f"acertos: {win} erros: {erro} rodadas: {vol}")
			if rep == 2:
				break
