comando = input("Digite um comando (iniciar, desligar, pausar): ")

match comando:
    case "iniciar":
        print("Ligando o sistema...")
    case "desligar":
        print("Desligando o sistema...")
    case "pausar":
        print("Sistema pausado.")
    case _:
        print("Comando inválido.")  # O '_' funciona como o 'default' do switch case