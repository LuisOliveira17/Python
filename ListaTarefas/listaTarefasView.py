escolha = 0
import listaTarefasUtils as utils
while True:

    if escolha == 6:
        break

    if escolha > 5:
        print("Insira um valor válido!!!!")

    print("-------Menu-------\n")
    print("1.Adicionar\n")
    print("2.Listar\n")
    print("3.Excluir\n")
    print("4.Concluir\n")
    print("5.Sair")
    print("---------------------")

    escolha = int(input("Escolha: "))

    match escolha:

        case 1:
            utils.addTarefa()

        case 2:
            utils.listarTarefas()

        case 3:
            utils.excluirTarefa()

        case 4:
            utils.concluirTarefa()

        case 5:
            print("FIM!!")
            break