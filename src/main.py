import flet as ft
import counter
import primeiros_passos
import rotas_e_navegacao

def carregar_menu(page: ft.Page):
    page.title = "Menu Flet"
    page.clean()

    page.add(
        ft.AppBar(title=ft.Text("Menu de Exercícios")),
        ft.ElevatedButton("Exercício: Contador", on_click=lambda e: counter.carregar_exercicio(page)),
        ft.ElevatedButton("Exercício: Primeiros Passos", on_click=lambda e: primeiros_passos.carregar_exercicio(page)),
        ft.ElevatedButton("Exercício: Rotas e Navegação", on_click=lambda e: rotas_e_navegacao.carregar_exercicio(page))
    )

def main(page: ft.Page):
    carregar_menu(page)

ft.app(target=main)
