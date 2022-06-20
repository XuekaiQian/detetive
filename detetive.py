print("Em uma sala de aula na pucpr um aluno foi morto, e assim o diretor da escola decidiu chamar você ,um grande detetive, para resolver o caso. Você determinou que os seguintes suspeitos estavam envolvidos no caso:")
print("1. Marcela, a namorada da vitima.")
print("2. Sofia, a melhor amiga de marcela.")
print("3. Rafaela, a professora de raciocinio algorítmico.")
print("4. Jhonatan, o professor de sistemas ciberfisicos.")
print("5. Rafael, o melhor aluno da sala.")
print("6. Luiz, o namorado de Sofia e melhor amigo da vitima.")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Apos uma meticulosa investigação você determinou o seguinte:")
print("1. A vitima foi assassinada de forma brutal na sala de aula, e você encontrou diversos hematomas de socos e chutes por todo seu corpo.")
print("2. Se Sofia estava na sala de aula no momento do assassinato, então Luiz o matou.")
print("3. Sofia ou Marcela estavam na sala de aula na hora e que a vitima foi espancada.")
print("4. Se Rafaela estava no lobby conversando com os alunos, então Jhonatan matou a vitima com uma facada.")
print("5. Se Rafaela não estava no lobby conversando com os alunos, então Marcela não estava na sala de aula quanto seu namorado morreu.")
print("6. Se Marcela estava na sala de aula no momento do assassinato, então  Rafael o matou.")
print("Agora você é o detetive, com as condições de cima, segue os passos e descobure quem é o assasino!")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
while True:
    start = int(input("Digite 1 para começar o jogo: "))
    if start == 1:
        print("Fale seu palpite")
        palpite1 = int(input("Qual foi a arma: 1.Pistola  2.Cano de chumbo  3.Veneno  4.Corda  5.Porrada  6.Faca   "))
        if palpite1 in range(1,7):
            palpite2 = int(input("Onde o vitima morreu: 1.lobby  2.sala de aula  "))
            if palpite2 in range(1, 3):
                palpite3 = int(input("Quem foi o assasino: 1.Marcela  2.Sofia  3.Rafaela  4.Jhonatan  5.Rafael  6.Luiz  "))
                if (palpite1 == 6 and palpite2 == 1 and palpite3 < 6) or (palpite1 < 6 and palpite2 == 2 and palpite3 < 6) or (palpite1 < 6 and palpite2 == 1 and palpite3 == 6):
                    print("Está certo 1/3.")
                    continue
                if (palpite1 == 6 and palpite2 == 2 and palpite3 < 6) or (palpite1 < 6 and palpite2 == 2 and palpite3 == 6) or (palpite1 == 6 and palpite2 == 1 and palpite3 == 6):
                    print("Está certo 2/3.")
                    continue
                if palpite1 and palpite2 and palpite3 == 6 and 2 and 6:
                    print("Sucesso!!!Você ganhou.")
                    print('''1. A —> B hip
2. A v C hip
3. D —> E hip
4. -D —> -C
5. C —> F
6. -E
7. -D   MT 3,6
8. -C.  MP 4,7
9. A.    SD 2,8
10. B.    MP 1,9''')
                    break