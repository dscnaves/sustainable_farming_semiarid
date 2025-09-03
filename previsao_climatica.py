from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from audio_util import falar

class PrevisaoClimaticaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Título
        layout.add_widget(Label(text='Previsão Climática (Próximos Dias)', font_size=28, size_hint_y=None, height=40))

        # Imagem ilustrativa
        layout.add_widget(Image(source='images/clima_variavel.png', size_hint_y=None, height=150))

        # Informações climáticas fictícias
        info_layout = BoxLayout(orientation='vertical', spacing=10)
        info_layout.add_widget(Label(text='Tendência: Redução de chuvas nos próximos 7 dias', font_size=20))
        info_layout.add_widget(Label(text='Risco de estiagem leve na região', font_size=20))
        info_layout.add_widget(Label(text='Temperatura média prevista: 35°C', font_size=20))
        info_layout.add_widget(Label(text='Umidade relativa esperada: 45%', font_size=20))
        info_layout.add_widget(Label(text='Recomendações: Reduzir irrigação nas horas mais quentes', font_size=20))

        scroll = ScrollView()
        scroll.add_widget(info_layout)
        layout.add_widget(scroll)

        # Botão de acessibilidade
        layout.add_widget(Button(
            text='Ouvir Informações',
            size_hint_y=None,
            height=50,
            on_press=self.ouvir_climatica
        ))

        # Botão voltar
        layout.add_widget(Button(text='Voltar à Página Inicial', size_hint_y=None, height=50, on_press=self.voltar))

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'home'

    def ouvir_climatica(self, instance):
        texto = (
            "Nos próximos dias, há tendência de redução de chuvas e risco de estiagem leve. "
            "A temperatura média será de trinta e cinco graus, e a umidade relativa em torno de quarenta e cinco por cento. "
            "Recomenda-se reduzir a irrigação nos horários de maior calor."
        )
        falar(texto)

