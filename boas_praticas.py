from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from audio_util import falar

class BoasPraticasScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Título
        layout.add_widget(Label(text='Boas Práticas de Cultivo', font_size=28, size_hint_y=None, height=40))

        # Imagem ilustrativa de técnica sustentável
        layout.add_widget(Image(source='images/cultivo_sustentavel.png', size_hint_y=None, height=160))

        # Conteúdo informativo
        dicas_layout = BoxLayout(orientation='vertical', spacing=10)
        dicas_layout.add_widget(Label(text='• Use cobertura vegetal no solo para evitar perda de umidade.', font_size=18))
        dicas_layout.add_widget(Label(text='• Evite irrigar entre 10h e 16h para reduzir evaporação.', font_size=18))
        dicas_layout.add_widget(Label(text='• Pratique rotação de culturas para preservar o solo.', font_size=18))
        dicas_layout.add_widget(Label(text='• Utilize técnicas de plantio em curva de nível.', font_size=18))
        dicas_layout.add_widget(Label(text='• Recicle restos de colheita como adubo orgânico.', font_size=18))

        scroll = ScrollView()
        scroll.add_widget(dicas_layout)
        layout.add_widget(scroll)

        # Botão de leitura por voz
        layout.add_widget(Button(
            text='Ouvir Dicas Sustentáveis',
            size_hint_y=None,
            height=50,
            on_press=self.ouvir_dicas
        ))
        # Botão voltar
        layout.add_widget(Button(text='Voltar à Página Inicial', size_hint_y=None, height=50, on_press=self.voltar))

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'home'

    def ouvir_dicas(self, instance):
        texto = (
            "Use cobertura vegetal para conservar a umidade do solo. "
            "Evite irrigar entre dez e dezesseis horas. "
            "Pratique rotação de culturas para melhorar a saúde do solo. "
            "Utilize o plantio em curvas de nível e recicle restos da colheita como adubo natural."
        )
        falar(texto)


