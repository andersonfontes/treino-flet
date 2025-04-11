# ATENÇÃO: execicios alterados pra implementr uso de VIEWS do flet, pra navegação adequada
# alterações nos comentarios

import flet as ft

def carregar_exercicio(page: ft.Page):  # main => carregar_exercicio
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.ElevatedButton("Voltar", on_click=lambda _: voltar_ao_menu(page)) #nova linha (botao voltar)
    )

# função de menu no próprio arquivo para usar como "voltar"
def voltar_ao_menu(page: ft.Page):
    page.views.clear()
    import main
    main.carregar_menu(page)