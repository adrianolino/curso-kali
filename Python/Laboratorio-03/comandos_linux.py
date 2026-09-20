import subprocess


def executar_comando(comando):
    print(f"\nExecutando: {' '.join(comando)}")

    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True
        )

        if resultado.returncode == 0:
            print("Status: SUCESSO")
            print("Saída:", resultado.stdout.strip())
        else:
            print("Status: ERRO")
            print("Erro:", resultado.stderr.strip())

    except FileNotFoundError:
        print("Status: COMANDO NÃO ENCONTRADO")


print("=" * 40)
print(" TESTE MÚLTIPLO DE COMANDOS")
print("=" * 40)

executar_comando(["whoami"])
executar_comando(["uname", "-r"])
executar_comando(["comando_inexistente"])

print("=" * 40)
