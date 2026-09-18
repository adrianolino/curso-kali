import os
import getpass
import platform
from datetime import datetime

print("=" * 40)
print("   DIAGNÓSTICO DO SISTEMA KALI")
print("=" * 40)

print(f"Usuário atual: {getpass.getuser()}")
print(f"Sistema: {platform.system()}")
print(f"Distribuição: {platform.platform()}")
print(f"Kernel: {platform.release()}")
print(f"Computador: {platform.node()}")
print(f"Data e hora: {datetime.now()}")

print("=" * 40)
