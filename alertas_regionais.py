from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from audio_util import falar

class AlertasRegionaisScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Título da tela
        layout.add_widget(Label(text='Alertas Regionais Climáticos', font_size=26))
    
        # Imagem de alerta
        layout.add_widget(Image(source='images/icone_alerta.png', size_hint_y=None, height=140))

        # Conteúdo dos alertas fictícios
        alertas_layout = BoxLayout(orientation='vertical', spacing=10)
        alertas_layout.add_widget(Label(text='• Risco de seca prolongada nas próximas semanas.'))
        alertas_layout.add_widget(Label(text='• Possibilidade de chuvas intensas em regiões vizinhas.'))
        alertas_layout.add_widget(Label(text='• Vento forte acima de 60 km/h previsto no fim de semana.'))
        alertas_layout.add_widget(Label(text='• Manter irrigação em áreas mais sombreadas.'))
        alertas_layout.add_widget(Label(text='• Proteja plantações sensíveis contra erosão e encharcamento.'))

        scroll = ScrollView()
        scroll.add_widget(alertas_layout)
        layout.add_widget(scroll)

        # Botão de leitura por voz
        layout.add_widget(Button(
            text='Ouvir Alertas',
            size_hint_y=None,
            height=50,
            on_press=self.ouvir_alertas
        ))

        # Botão para voltar à tela inicial
        layout.add_widget(Button(
            text='Voltar à Página Inicial',
            size_hint_y=None,
            height=50,
            on_press=self.voltar
        ))

        self.add_widget(layout)

    def ouvir_alertas(self, instance):
        texto = (
            "Alertas regionais: risco de seca nas próximas semanas. Chuvas intensas podem ocorrer em áreas próximas. "
            "Previsão de ventos fortes acima de sessenta quilômetros por hora neste fim de semana. "
            "Irrigue áreas sombreadas e proteja plantações sensíveis contra erosão."
        )
        falar(texto)

    def voltar(self, instance):
        self.manager.current = 'home'
