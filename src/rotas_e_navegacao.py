# ATENÇÃO: execicios alterados pra implementr uso de VIEWS do flet, pra navegação adequada
# alterações nos comentarios laterais

# A rota da página é uma parte da URL do aplicativo após o símbolo:#
# A rota padrão do aplicativo, se não for definida na URL do aplicativo pelo usuário, é . Todas as rotas começam com , por exemplo , .///store/authors/1/books/2
# A rota do aplicativo pode ser obtida lendo a propriedade, por exemplo:page.route

# import flet as ft

# def main(page: ft.Page):
#     page.add(ft.Text(f"Initial route: {page.route}"))

# ft.app(main, view=ft.AppView.WEB_BROWSER)




# Toda vez que a rota na URL é alterada (editando a URL ou navegando no histórico do navegador com os botões Voltar/Avançar), o Flet chama o manipulador de eventos:page.on_route_change
# import flet as ft

# def main(page: ft.Page):
#     page.add(ft.Text(f"Rota Inicial: {page.route}"))

#     def route_change(e: ft.RouteChangeEvent):
#         page.add(ft.Text(f"Nova rota: {e.route}"))

#     page.on_route_change = route_change
#     page.update()

# ft.app(main, view=ft.AppView.WEB_BROWSER)





# A rota pode ser alterada programaticamente, atualizando a propriedade:page.route
# import flet as ft

# def main(page: ft.Page):
#     page.add(ft.Text(f"Rota inicial: {page.route}"))

#     def route_change(e: ft.RouteChangeEvent):
#         page.add(ft.Text(f"Nova Rota: {e.route}"))

#     def go_store(e):
#         page.route = "/loja"
#         page.update()

#     page.on_route_change = route_change
#     page.add(ft.ElevatedButton("Ir à loja", on_click=go_store))

# ft.app(main, view=ft.AppView.WEB_BROWSER)



# Visualizações de página
# O Flet's Page agora não é apenas uma única página, mas um contêiner para View em camadas umas sobre as outras como um sanduíche:
# Uma coleção de visualizações representa o histórico do navegador. Page tem a propriedade page.views para acessar a coleção de exibições.
# A última visualização na lista é a que está sendo exibida atualmente em uma página. A lista de exibições deve ter pelo menos um elemento (exibição raiz).
# Para simular uma transição entre páginas, altere e adicione uma nova no final da lista.page.routeViewpage.view
# Retire a última exibição da coleção e altere a rota para uma "anterior" em page.on_view_pop manipulador de eventos para voltar.

# Construindo visualizações sobre a mudança de rota
# Para construir uma navegação confiável, deve haver um único local no programa que cria uma lista de visualizações, dependendo da rota atual. Em outras palavras, a pilha de histórico de navegação (representada pela lista de visualizações) deve ser uma função de uma rota.
# Esse local é page.on_route_change manipulador de eventos.
# Vamos juntar tudo em um exemplo completo que permite navegar entre duas páginas:

# ATENÇÃO: execicios alterados pra implementr uso de VIEWS do flet, pra navegação adequada
# alterações nos comentarios laterais

import flet as ft

def carregar_exercicio(page: ft.Page):  # main => carregar_exercicio
    page.title = "Exemplo de rotas"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store"))
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ft.ElevatedButton("Voltar ao menu", on_click=lambda _: voltar_ao_menu(page)),  # volta pro menu
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


# ft.app(main, view=ft.AppView.WEB_BROWSER) 

def voltar_ao_menu(page: ft.Page):
    page.views.clear()
    import main
    main.carregar_menu(page)
