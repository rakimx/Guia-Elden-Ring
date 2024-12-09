from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton

class BossCard(MDCard):
    def __init__(self, boss_name, image_source, description, location_image, screen_manager, tactics_text, tactics_image, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = "8dp"
        self.size_hint_y = None
        self.height = "200dp"
        self.md_bg_color = "grey"
        self.boss_name = boss_name
        self.description = description
        self.image_source = image_source
        self.location_image = location_image
        self.screen_manager = screen_manager
        self.tactics_text = tactics_text
        self.tactics_image = tactics_image

        self.image = Image(source=image_source, allow_stretch=True)
        self.add_widget(self.image)

        self.label = MDLabel(text=boss_name, halign="center", theme_text_color="Custom", text_color="white")
        self.add_widget(self.label)

    def on_release(self):
        self.screen_manager.current = 'boss_details'
        self.screen_manager.get_screen('boss_details').update_boss_details(
            self.boss_name, self.image_source, self.description, self.location_image, self.tactics_text, self.tactics_image
        )

class MainScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.bosses = {
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

        scroll_view = MDScrollView()
        grid_layout = MDGridLayout(cols=2, spacing="10dp", padding="10dp", adaptive_height=True)

        for boss_name, boss_data in self.bosses.items():
            card = BossCard(boss_name, boss_data["image"], boss_data["description"], boss_data["location_image"], self.screen_manager, boss_data["tactics_text"], boss_data["tactics_image"])
            grid_layout.add_widget(card)

        scroll_view.add_widget(grid_layout)
        self.add_widget(scroll_view)

class BossDetailsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.boss_name_label = MDLabel(halign="center", theme_text_color="Custom", text_color="white", font_style="H4")
        self.boss_image = Image()
        self.boss_description_label = MDLabel(halign="center", theme_text_color="Primary")
        self.location_image = None
        self.tactics_text = None
        self.tactics_image = None

        self.location_button = MDRectangleFlatButton(
            text="Localização",
            on_release=self.mostrar_localizacao,
            pos_hint={"center_x": 0.5}
        )

        self.tacticas_button = MDRectangleFlatButton(
            text="Táticas",
            on_release=self.mostrar_tacticas,
            pos_hint={"center_x": 0.5}
        )

        self.voltar_button = MDRectangleFlatButton(
            text="Voltar",
            on_release=self.voltar_para_main,
            pos_hint={"center_x": 0.5}
        )

        layout = MDBoxLayout(orientation="vertical", spacing="10dp", padding="10dp")
        layout.add_widget(self.boss_name_label)
        layout.add_widget(self.boss_image)
        layout.add_widget(self.boss_description_label)
        layout.add_widget(self.location_button)
        layout.add_widget(self.tacticas_button)
        layout.add_widget(self.voltar_button)
        self.add_widget(layout)

    def update_boss_details(self, boss_name, image_source, description, location_image, tactics_text, tactics_image):
        self.boss_name_label.text = boss_name
        self.boss_image.source = image_source
        self.boss_description_label.text = description
        self.location_image = location_image
        self.tactics_text = tactics_text
        self.tactics_image = tactics_image

    def voltar_para_main(self, instance):
        self.manager.current = 'main'

    def mostrar_localizacao(self, instance):
        self.manager.current = 'location_screen'
        self.manager.get_screen('location_screen').update_location_image(self.location_image)

    def mostrar_tacticas(self, instance):
        self.manager.current = 'tactics_screen'
        self.manager.get_screen('tactics_screen').update_tactics_text(self.tactics_text, self.tactics_image)

class LocationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.location_image = Image(allow_stretch=True)

        layout = MDBoxLayout(orientation="vertical")
        layout.add_widget(self.location_image)

        voltar_button = MDRectangleFlatButton(
            text="Voltar",
            on_release=self.voltar_para_detalhes,
            pos_hint={"center_x": 0.5}
        )
        layout.add_widget(voltar_button)

        self.add_widget(layout)

    def update_location_image(self, image_source):
        self.location_image.source = image_source

    def voltar_para_detalhes(self, instance):
        self.manager.current = 'boss_details'

class TacticsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tactics_label = MDLabel(theme_text_color="Primary", halign="center", valign="top")
        self.tactics_image = Image(allow_stretch=True, size_hint=(1, None), height=200)  # Usa Image para a imagem estática

        layout = MDBoxLayout(orientation="vertical", spacing="10dp", padding="10dp")
        layout.add_widget(self.tactics_label)
        layout.add_widget(self.tactics_image)

        voltar_button = MDRectangleFlatButton(
            text="Voltar",
            on_release=self.voltar_para_detalhes,
            pos_hint={"center_x": 0.5}
        )
        layout.add_widget(voltar_button)

        self.add_widget(layout)

    def update_tactics_text(self, text, image_source):
        self.tactics_label.text = text
        self.tactics_image.source = image_source
        self.tactics_image.reload()

    def voltar_para_detalhes(self, instance):
        self.manager.current = 'boss_details'

class EldenRingApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main', screen_manager=sm))
        sm.add_widget(BossDetailsScreen(name='boss_details'))
        sm.add_widget(LocationScreen(name='location_screen'))
        sm.add_widget(TacticsScreen(name='tactics_screen'))
        return sm

if __name__ == '__main__':
    EldenRingApp().run()