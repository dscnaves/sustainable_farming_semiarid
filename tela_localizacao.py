import os
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from audio_util import falar

class TelaLocalizacao(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Título
        layout.add_widget(Label(text='Digite sua cidade no formato:\nCampinas - SP, Brasil', font_size=22))
        
        # Imagem representando localização
        layout.add_widget(Image(source='images/icone_localizacao.png', size_hint_y=None, height=140))

        # Campo para entrada da cidade
        self.input_local = TextInput(hint_text='Exemplo: Juazeiro - BA, Brasil', font_size=18, multiline=False)
        layout.add_widget(self.input_local)

        # Carrega localização salva anteriormente
        self.carregar_localidade()

        # Botão para leitura por voz
        layout.add_widget(Button(
            text='Ouvir Orientações',
            size_hint_y=None,
            height=50,
            on_press=self.ouvir_orientacoes
        ))

        # Botão para salvar cidade
        layout.add_widget(Button(
            text='Salvar Localidade',
            size_hint_y=None,
            height=50,
            on_press=self.salvar_localidade
        ))

        # Botão para voltar à tela inicial
        layout.add_widget(Button(
            text='Voltar à Tela Inicial',
            size_hint_y=None,
            height=50,
            on_press=self.voltar
        ))

        self.add_widget(layout)

    def ouvir_orientacoes(self, instance):
        texto = (
            "Digite sua cidade no formato: nome da cidade, traço, sigla do estado, vírgula e Brasil. "
            "Por exemplo: Campinas - SP, Brasil. Em seguida, clique em salvar."
        )
        falar(texto)

    def salvar_localidade(self, instance=None):
        local = self.input_local.text.strip()
        if local:
            with open("localidade.txt", "w", encoding="utf-8") as f:
                f.write(local)
            self.mostrar_popup("Localidade salva com sucesso!")
        else:
            self.mostrar_popup("Por favor, digite uma localidade válida.")

    def carregar_localidade(self):
        if os.path.exists("localidade.txt"):
            with open("localidade.txt", "r", encoding="utf-8") as f:
                self.input_local.text = f.read()

    def mostrar_popup(self, mensagem):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=mensagem))
        btn = Button(text='Fechar', size_hint_y=None, height=40)
        popup = Popup(title='Aviso', content=content, size_hint=(None, None), size=(300, 200))
        btn.bind(on_press=popup.dismiss)
        content.add_widget(btn)
        popup.open()

    def voltar(self, instance):
        self.manager.current = 'home'
