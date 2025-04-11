import flet as ft
import subprocess
import sys
import os
import random

porta_livre = random.randint(8600, 8700) # acha uma porta livre 



def main(page: ft.Page):
    page.title = "Menu Inicial"

    def abrir_counter(e):
        # Garante que vai usar o mesmo Python e caminho absoluto do script
        python_exec = sys.executable
        caminho = os.path.abspath("src/counter.py")
        subprocess.Popen([python_exec, caminho])

    page.add(
        ft.AppBar(title=ft.Text("Menu Inicial")),
        ft.ElevatedButton("Abrir Contador", on_click=abrir_counter)
    )

ft.app(target=main, view=ft.FLET_APP, port=8701)
