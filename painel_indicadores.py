from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from audio_util import falar

class PainelIndicadoresScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=15, padding=20)

        # Título
        layout.add_widget(Label(text='Painel de Indicadores Ambientais', font_size=26))

        # Ícone ilustrativo
        layout.add_widget(Image(source='images/icone_indicadores.png', size_hint_y=None, height=140))

        # Indicadores simulados
        indicadores = [
            "Temperatura média mensal: 30.2°C",
            "Umidade relativa: 52%",
            "Índice de Seca (SPI): -0.8 → Moderado",
            "Velocidade média do vento: 12 km/h",
            "Radiação solar diária: 5.4 kWh/m²",
            "Precipitação acumulada no mês: 43 mm",
        ]

        for indicador in indicadores:
            layout.add_widget(Label(text=indicador, font_size=18))

        # Botão para ouvir os dados
        layout.add_widget(Button(
            text='Ouvir Indicadores',
            size_hint_y=None,
            height=50,
            on_press=self.ouvir_indicadores
        ))

        # Botão para voltar
        layout.add_widget(Button(
            text='Voltar à Tela Inicial',
            size_hint_y=None,
            height=50,
            on_press=self.voltar
        ))

        self.add_widget(layout)

    def ouvir_indicadores(self, instance):
        texto = (
            "Indicadores ambientais da sua região: temperatura média de trinta graus Celsius, "
            "umidade de cinquenta e dois por cento, índice de seca moderado, vento médio de doze quilômetros por hora, "
            "radiação solar diária de cinco ponto quatro kilowatt-hora por metro quadrado e chuva acumulada de quarenta e três milímetros no mês."
        )
        falar(texto)

    def voltar(self, instance):
        self.manager.current = 'home'
