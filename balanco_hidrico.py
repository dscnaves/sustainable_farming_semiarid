from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from audio_util import falar

class BalancoHidricoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Título
        layout.add_widget(Label(text='Balanço Hídrico do Solo', font_size=28, size_hint_y=None, height=40))

        # Imagem representativa do solo úmido
        layout.add_widget(Image(source='images/balanco_hidrico_solo.png', size_hint_y=None, height=160))

        # Dados fictícios para exemplo visual
        dados_layout = BoxLayout(orientation='vertical', spacing=10)
        dados_layout.add_widget(Label(text='Nível de Umidade do Solo: 72%', font_size=20))
        dados_layout.add_widget(Label(text='Capacidade de Armazenamento: 180 mm', font_size=20))
        dados_layout.add_widget(Label(text='Evapotranspiração: 3.2 mm/dia', font_size=20))
        dados_layout.add_widget(Label(text='Índice de Seca Atual: Moderado', font_size=20))
        dados_layout.add_widget(Label(text='Recomendações: Irrigar apenas no início da manhã', font_size=20))
        dados_layout.add_widget(Label(text='Evite o uso de máquinas em áreas alagadas', font_size=20))

        scroll = ScrollView()
        scroll.add_widget(dados_layout)
        layout.add_widget(scroll)

        # Botão de leitura por voz
        layout.add_widget(Button(
            text='Ouvir Informações',
            size_hint_y=None,
            height=50,
            on_press=self.ouvir_balanco
        ))

        # Botão voltar
        layout.add_widget(Button(text='Voltar à Página Inicial', size_hint_y=None, height=50, on_press=self.voltar))

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'home'

    def ouvir_balanco(self, instance):
        texto = (
            "O solo apresenta umidade de setenta e dois por cento, com capacidade de armazenamento de cento e oitenta milímetros. "
            "Evapotranspiração está em três ponto dois milímetros por dia. O índice de seca é moderado. "
            "Evite o uso de máquinas em áreas encharcadas e irrigue preferencialmente pela manhã."
        )
        falar(texto)
