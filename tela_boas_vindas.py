from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from audio_util import falar

class TelaBoasVindas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Imagem de introdução
        layout.add_widget(Image(source='images/sertao_intro.png', size_hint_y=None, height=220))

        # Mensagem de boas-vindas
        layout.add_widget(Label(
            text='Bem-vindo ao Sertão Sustentável!\nJuntos pela força do sertão!',
            font_size=24,
            halign='center',
            valign='middle'
        ))

        # Botão de leitura por voz
        layout.add_widget(Button(
            text='Ouvir Mensagem',
            size_hint_y=None,
            height=50,
            on_press=self.ouvir_mensagem
        ))

        # Botão para entrar no app
        layout.add_widget(Button(text='Entrar no App', size_hint_y=None, height=60, on_press=self.entrar))

        self.add_widget(layout)

    def entrar(self, instance):
        self.manager.current = 'home'

    def ouvir_mensagem(self, instance):
        texto = "Bem-vindo ao Sertão Sustentável! Juntos pela força do sertão, pela terra e pela esperança."
        falar(texto)

