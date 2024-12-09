from kivy.uix.image import Image  # Importa a classe Image para exibir imagens
from kivymd.app import MDApp  # Importa a classe MDApp para criar o aplicativo
from kivy.uix.screenmanager import ScreenManager, Screen  # Importa as classes ScreenManager e Screen para gerenciar as telas
from kivymd.uix.card import MDCard  # Importa a classe MDCard para criar os cards dos chefes
from kivymd.uix.label import MDLabel  # Importa a classe MDLabel para criar os labels
from kivymd.uix.scrollview import MDScrollView  # Importa a classe MDScrollView para criar a área de rolagem
from kivymd.uix.gridlayout import MDGridLayout  # Importa a classe MDGridLayout para organizar os cards em uma grade
from kivymd.uix.boxlayout import MDBoxLayout  # Importa a classe MDBoxLayout para organizar os elementos nas telas
from kivymd.uix.button import MDRectangleFlatButton  # Importa a classe MDRectangleFlatButton para criar botões

class BossCard(MDCard):  # Define a classe BossCard que herda de MDCard
    def __init__(self, boss_name, image_source, description, location_image, screen_manager, tactics_text, tactics_image, **kwargs):
        super().__init__(**kwargs)  # Inicializa a classe pai (MDCard)
        self.orientation = "vertical"  # Define a orientação do card como vertical
        self.padding = "8dp"  # Define o espaçamento interno do card
        self.size_hint_y = None  # Define que o tamanho vertical do card será definido pela altura
        self.height = "200dp"  # Define a altura do card
        self.md_bg_color = "grey"  # Define a cor de fundo do card como cinza
        self.boss_name = boss_name  # Armazena o nome do chefe
        self.description = description  # Armazena a descrição do chefe
        self.image_source = image_source  # Armazena o caminho da imagem do chefe
        self.location_image = location_image  # Armazena o caminho da imagem de localização do chefe
        self.screen_manager = screen_manager  # Armazena o gerenciador de telas
        self.tactics_text = tactics_text  # Armazena o texto das táticas
        self.tactics_image = tactics_image  # Armazena o caminho da imagem das táticas

        self.image = Image(source=image_source, allow_stretch=True)  # Cria a imagem do chefe
        self.add_widget(self.image)  # Adiciona a imagem ao card

        self.label = MDLabel(text=boss_name, halign="center", theme_text_color="Custom", text_color="white")  # Cria o label com o nome do chefe
        self.add_widget(self.label)  # Adiciona o label ao card

    def on_release(self):
        # Ao clicar no card, muda para a tela de detalhes do chefe e atualiza as informações
        self.screen_manager.current = 'boss_details'
        self.screen_manager.get_screen('boss_details').update_boss_details(
            self.boss_name, self.image_source, self.description, self.location_image, self.tactics_text, self.tactics_image
        )

class MainScreen(Screen):  # Define a classe MainScreen que herda de Screen
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)  # Inicializa a classe pai (Screen)
        self.screen_manager = screen_manager  # Armazena o gerenciador de telas
        self.bosses = {  # Dicionário com as informações dos chefes
            "Godrick, o Enxertado": {
                "image": "imagens/godrick.jpg",
                "description": "Um semideus que se enxertou com partes de outros seres.",
                "location_image": "imagens/godrick_loc.jpg",
                "tactics_text": "Para derrotar Godrick, o Enxertado, explore o uso de ataques de fogo, aproveitando sua fraqueza a esse elemento. Concentre-se em esquivar de seus golpes de longo alcance e aproveite as oportunidades para atacá-lo pelas costas durante suas longas animações.",
                "tactics_image": "imagens/godrick_tactics.jpg",
            },
            "Rennala, Rainha da Lua Cheia": {
                "image": "imagens/rennala.jpg",
                "description": "Uma poderosa feiticeira que reside na Academia de Raya Lucaria.",
                "location_image": "imagens/rennala_loc.jpg",
                "tactics_text": "Rennala apresenta duas fases distintas. Na primeira, ataque os alunos para romper sua barreira protetora. Na segunda fase, priorize a esquiva de seus feitiços e aproveite os momentos de vulnerabilidade para contra-atacar.",
                "tactics_image": "imagens/rennala_tactics.jpg",
            },
            "Radahn, Flagelo das Estrelas": {
                "image": "imagens/radahn.jpg",
                "description": "Um poderoso guerreiro que aprendeu a gravitação para conter as estrelas.",
                "location_image": "imagens/radahn_loc.jpg",
                "tactics_text": "Use as invocações para distraí-lo e ataque com golpes fortes. Utilize a magia de podridão escarlate para causar dano adicional.",
                "tactics_image": "imagens/radahn_tactics.jpg",
            },
            "Rykard, Senhor da Blasfêmia": {
                "image": "imagens/rykard.jpg",
                "description": "Um semideus que se fundiu a uma serpente gigante.",
                "location_image": "imagens/rykard_loc.jpg",
                "tactics_text": "Equipe a lança Serpent-Hunter e utilize seus ataques especiais para causar dano massivo. Mantenha distância e desvie de seus ataques de fogo.",
                "tactics_image": "imagens/rykard_tactics.jpg",
            },
            "Morgott, o Rei Agouro": {
                "image": "imagens/morgott.jpg",
                "description": "O rei de Leyndell, a Capital Real.",
                "location_image": "imagens/morgott_loc.jpg",
                "tactics_text": "Cuidado com seus ataques sagrados e golpes de espada. Utilize invocações para distraí-lo e aproveite as aberturas para atacar.",
                "tactics_image": "imagens/morgott_tactics.jpg",
            },
            "Gigante de Fogo": {
                "image": "imagens/fire_giant.jpg",
                "description": "Um gigante que guarda a entrada para as Montanhas dos Gigantes.",
                "location_image": "imagens/fire_giant_loc.jpg",
                "tactics_text": "Concentre seus ataques nas pernas para derrubá-lo e então ataque sua cabeça. Utilize magias e encantamentos para causar dano à distância.",
                "tactics_image": "imagens/fire_giant_tactics.jpg",
            },
            "Malenia, Lâmina de Miquella": {
                "image": "imagens/malenia.jpg",
                "description": "Uma guerreira habilidosa que empunha uma katana mortal.",
                "location_image": "imagens/malenia_loc.jpg",
                "tactics_text": "Evite seus combos rápidos e utilize ataques com sangramento. Utilize invocações para distraí-la e aproveite as janelas de oportunidade para atacar.",
                "tactics_image": "imagens/malenia_tactics.jpg",
            },
            "Godfrey, Primeiro Lorde Élfico": {
                "image": "imagens/godfrey.jpg",
                "description": "O primeiro Lorde Élfico e um guerreiro lendário.",
                "location_image": "imagens/godfrey_loc.jpg",
                "tactics_text": "Cuidado com seus ataques de machado e golpes corpo-a-corpo. Desvie de seus ataques e contra-ataque quando ele estiver vulnerável.",
                "tactics_image": "imagens/godfrey_tactics.jpg",
            },
            "Radagon da Ordem Áurea": {
                "image": "imagens/radagon.jpg",
                "description": "O segundo marido de Marika, a Deusa Eterna.",
                "location_image": "imagens/radagon_loc.jpg",
                "tactics_text": "Evite seus ataques sagrados e de martelo. Utilize magias e encantamentos para causar dano à distância e aproveite as aberturas para atacar.",
                "tactics_image": "imagens/radagon_tactics.jpg",
            },
            "Besta Ancestral": {
                "image": "imagens/elden_beast.jpg",
                "description": "A besta que personifica a Grande Vontade.",
                "location_image": "imagens/elden_beast_loc.jpg",
                "tactics_text": "Use ataques sagrados e evite seus ataques de área. Mantenha distância e utilize magias e encantamentos para causar dano.",
                "tactics_image": "imagens/elden_beast_tactics.jpg",
            },
        }

        scroll_view = MDScrollView()  # Cria um scrollview para permitir a rolagem na tela
        grid_layout = MDGridLayout(cols=2, spacing="10dp", padding="10dp", adaptive_height=True)  # Define o layout da grade para os cards

        # Cria os cards dos chefes e os adiciona ao layout
        for boss_name, boss_data in self.bosses.items():
            card = BossCard(boss_name, boss_data["image"], boss_data["description"], boss_data["location_image"], self.screen_manager, boss_data["tactics_text"], boss_data["tactics_image"])
            grid_layout.add_widget(card)

        scroll_view.add_widget(grid_layout)  # Adiciona o layout da grade ao scrollview
        self.add_widget(scroll_view)  # Adiciona o scrollview à tela

class BossDetailsScreen(Screen):  # Define a classe BossDetailsScreen que herda de Screen
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Inicializa a classe pai (Screen)
        self.boss_name_label = MDLabel(halign="center", theme_text_color="Custom", text_color="white", font_style="H4")  # Cria o label para o nome do chefe
        self.boss_image = Image()  # Cria a imagem do chefe
        self.boss_description_label = MDLabel(halign="center", theme_text_color="Primary")  # Cria o label para a descrição do chefe
        self.location_image = None  # Inicializa a variável para a imagem de localização
        self.tactics_text = None  # Inicializa a variável para o texto de táticas
        self.tactics_image = None  # Inicializa a variável para a imagem de táticas

        self.location_button = MDRectangleFlatButton(  # Cria o botão de localização
            text="Localização",
            on_release=self.mostrar_localizacao,  # Define a função a ser chamada ao clicar no botão
            pos_hint={"center_x": 0.5}  # Define a posição do botão
        )

        self.tacticas_button = MDRectangleFlatButton(  # Cria o botão de táticas
            text="Táticas",
            on_release=self.mostrar_tacticas,  # Define a função a ser chamada ao clicar no botão
            pos_hint={"center_x": 0.5}  # Define a posição do botão
        )

        self.voltar_button = MDRectangleFlatButton(  # Cria o botão de voltar
            text="Voltar",
            on_release=self.voltar_para_main,  # Define a função a ser chamada ao clicar no botão
            pos_hint={"center_x": 0.5}  # Define a posição do botão
        )

        layout = MDBoxLayout(orientation="vertical", spacing="10dp", padding="10dp")  # Define o layout da tela de detalhes
        # Adiciona os widgets ao layout
        layout.add_widget(self.boss_name_label)
        layout.add_widget(self.boss_image)
        layout.add_widget(self.boss_description_label)
        layout.add_widget(self.location_button)
        layout.add_widget(self.tacticas_button)
        layout.add_widget(self.voltar_button)
        self.add_widget(layout)  # Adiciona o layout à tela

    def update_boss_details(self, boss_name, image_source, description, location_image, tactics_text, tactics_image):
        # Atualiza as informações do chefe na tela de detalhes
        self.boss_name_label.text = boss_name
        self.boss_image.source = image_source
        self.boss_description_label.text = description
        self.location_image = location_image
        self.tactics_text = tactics_text
        self.tactics_image = tactics_image

    def voltar_para_main(self, instance):
        self.manager.current = 'main'  # Volta para a tela principal

    def mostrar_localizacao(self, instance):
        # Muda para a tela de localização e atualiza a imagem
        self.manager.current = 'location_screen'
        self.manager.get_screen('location_screen').update_location_image(self.location_image)

    def mostrar_tacticas(self, instance):
        # Muda para a tela de táticas e atualiza o texto e a imagem
        self.manager.current = 'tactics_screen'
        self.manager.get_screen('tactics_screen').update_tactics_text(self.tactics_text, self.tactics_image)

class LocationScreen(Screen):  # Define a classe LocationScreen que herda de Screen
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Inicializa a classe pai (Screen)
        self.location_image = Image(allow_stretch=True)  # Cria a imagem de localização

        layout = MDBoxLayout(orientation="vertical")  # Define o layout da tela de localização
        layout.add_widget(self.location_image)  # Adiciona a imagem ao layout

        voltar_button = MDRectangleFlatButton(  # Cria o botão de voltar
            text="Voltar",
            on_release=self.voltar_para_detalhes,  # Define a função a ser chamada ao clicar no botão
            pos_hint={"center_x": 0.5}  # Define a posição do botão
        )
        layout.add_widget(voltar_button)  # Adiciona o botão ao layout

        self.add_widget(layout)  # Adiciona o layout à tela

    def update_location_image(self, image_source):
        self.location_image.source = image_source  # Atualiza a imagem de localização

    def voltar_para_detalhes(self, instance):
        self.manager.current = 'boss_details'  # Volta para a tela de detalhes do chefe

class TacticsScreen(Screen):  # Define a classe TacticsScreen que herda de Screen
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Inicializa a classe pai (Screen)
        self.tactics_label = MDLabel(theme_text_color="Primary", halign="center", valign="top")  # Cria o label para o texto de táticas
        self.tactics_image = Image(allow_stretch=True, size_hint=(1, None), height=200)  # Cria a imagem de táticas

        layout = MDBoxLayout(orientation="vertical", spacing="10dp", padding="10dp")  # Define o layout da tela de táticas
        layout.add_widget(self.tactics_label)  # Adiciona o label ao layout
        layout.add_widget(self.tactics_image)  # Adiciona a imagem ao layout

        voltar_button = MDRectangleFlatButton(  # Cria o botão de voltar
            text="Voltar",
            on_release=self.voltar_para_detalhes,  # Define a função a ser chamada ao clicar no botão
            pos_hint={"center_x": 0.5}  # Define a posição do botão
        )
        layout.add_widget(voltar_button)  # Adiciona o botão ao layout

        self.add_widget(layout)  # Adiciona o layout à tela

    def update_tactics_text(self, text, image_source):
        # Atualiza o texto e a imagem de táticas
        self.tactics_label.text = text
        self.tactics_image.source = image_source
        self.tactics_image.reload()  # Recarrega a imagem

    def voltar_para_detalhes(self, instance):
        self.manager.current = 'boss_details'  # Volta para a tela de detalhes do chefe

class EldenRingApp(MDApp):  # Define a classe EldenRingApp que herda de MDApp
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Define o tema do aplicativo como escuro
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main', screen_manager=sm))
        sm.add_widget(BossDetailsScreen(name='boss_details'))
        sm.add_widget(LocationScreen(name='location_screen'))
        sm.add_widget(TacticsScreen(name='tactics_screen'))
        return sm

if __name__ == '__main__':
    EldenRingApp().run()