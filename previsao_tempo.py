from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from audio_util import falar

class PrevisaoTempoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Título da tela
        layout.add_widget(Label(text='Previsão do Tempo', font_size=28, size_hint_y=None, height=40))

        # Ícone do tempo
        layout.add_widget(Image(source='images/tempo_sol_nuvem.png', size_hint_y=None, height=150))

        # Informações do clima
        clima_layout = BoxLayout(orientation='vertical', spacing=10)
        clima_layout.add_widget(Label(text='Temperatura: <SERÁ INTEGRADO AO BACKEND>', font_size=20))
        clima_layout.add_widget(Label(text='Umidade: <SERÁ INTEGRADO AO BACKEND>', font_size=20))
        clima_layout.add_widget(Label(text='Velocidade do Vento: <SERÁ INTEGRADO AO BACKEND>', font_size=20))
        clima_layout.add_widget(Label(text='Chance de Chuva: <SERÁ INTEGRADO AO BACKEND>', font_size=20))

        scroll = ScrollView()
        scroll.add_widget(clima_layout)
        layout.add_widget(scroll)

        # Botão de acessibilidade com ícone de megafone
        layout.add_widget(Button(
            text='Ouvir Informações',
            size_hint_y=None,
            height=50,
            on_press=self.ouvir_clima
            ))

        # Botão voltar
        layout.add_widget(Button(text='Voltar à Página Inicial', size_hint_y=None, height=50, on_press=self.voltar))

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'home'

    def ouvir_clima(self, instance):
        texto = (
            "Previsão do tempo para hoje: "
            "Temperatura de trinta e dois graus Celsius, "
            "umidade relativa de cinquenta e oito por cento, "
            "vento a quatorze quilômetros por hora. "
            "Chance de chuva é de vinte por cento."
        )
        falar(texto)


    

