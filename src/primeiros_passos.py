# ATENÇÃO: execicios alterados pra implementr uso de VIEWS do flet, pra navegação adequada
# alterações nos comentarios

import flet as ft


def carregar_exercicio(page: ft.Page):  # main => carregar_exercicio
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):  # funcao original do exemplo quando vc da o flet create
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    def decrement_click(e): # criei esta funcao pra usar no botao de -
        counter.data -= 1
        counter.value = str(counter.data)
        counter.update()    

    page.floating_action_button = ft.FloatingActionButton(  # cria o botao de +
        icon=ft.Icons.ADD, on_click=increment_click
    )
    # page.floating_action_button = ft.FloatingActionButton( # substituiu o botao +, ao inves de criar outro => arrumar
    #     icon=ft.Icons.REMOVE, on_click=decrement_click
    # )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),            
            expand=True,
        )
    )

    t = ft.Text(value="Hello, world!", color="green",bgcolor="white")  
    page.controls.append(t)    # forma 1: crio o controle, depois "apendo", depois atualiza o objeto pagina
    page.update()

    page.add(                 # forma 2: utiliza o page.add pra ja adicionar o objeto na pagina
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ])
)
    page.add(
    ft.Card(
        ft.Row(controls=[             # inserindo um campo com um botao do lado
            ft.TextField(label="Seu nome", width=500),     # brincando e conhecendo algumas propriedades dos controles
            ft.ElevatedButton(text="Diga meu nome!", width=250)
        ], alignment="center", expand=True)
    )  ,
        ft.ElevatedButton("Voltar", on_click=lambda _: voltar_ao_menu(page)) #nova linha (botao voltar)
)



# função de menu no próprio arquivo para usar como "voltar"
def voltar_ao_menu(page: ft.Page):
    page.views.clear()
    import main
    main.carregar_menu(page)