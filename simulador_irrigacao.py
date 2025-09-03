from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from audio_util import falar

class SimuladorIrrigacaoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Título da tela
        layout.add_widget(Label(text='Simulador de Irrigação Inteligente', font_size=26))

        # Imagem após o título
        layout.add_widget(Image(source='images/icone_irrigacao.png', size_hint_y=None, height=140))

        # Campo para seleção do tipo de cultivo
        self.spinner_cultura = Spinner(
            text='Selecione o cultivo',
            values=['Feijão', 'Milho', 'Palma Forrageira', 'Mandioca'],
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.spinner_cultura)

        # Seleção do tipo de solo
        self.spinner_solo = Spinner(
            text='Tipo de solo',
            values=['Arenoso', 'Argiloso', 'Siltoso'],
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.spinner_solo)

        # Entrada de evapotranspiração média
        self.input_evapo = TextInput(
            hint_text='Evapotranspiração diária (mm)',
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.input_evapo)

        # Botão para calcular
        layout.add_widget(Button(
            text='Calcular Volume Ideal (litros/dia)',
            size_hint_y=None,
            height=50,
            on_press=self.calcular_irrigacao
        ))

        # Resultado
        self.resultado = Label(text='', font_size=18)
        layout.add_widget(self.resultado)

        # Botão de leitura em voz
        layout.add_widget(Button(
            text='Ouvir Recomendação',
            size_hint_y=None,
            height=50,
            on_press=self.ouvir_recomendacao
        ))

        # Botão de retorno
        layout.add_widget(Button(
            text='Voltar à Tela Inicial',
            size_hint_y=None,
            height=50,
            on_press=self.voltar
        ))

        self.add_widget(layout)

    def calcular_irrigacao(self, instance):
        cultura = self.spinner_cultura.text
        solo = self.spinner_solo.text
        try:
            evapo = float(self.input_evapo.text)
        except ValueError:
            self.resultado.text = "Digite um valor numérico para evapotranspiração."
            return

        # Fatores baseados em tipo de solo
        fator_solo = {
            'Arenoso': 1.2,
            'Argiloso': 0.8,
            'Siltoso': 1.0
        }.get(solo, 1.0)

        # Demanda hídrica por cultura (simulada)
        demanda_base = {
            'Feijão': 3.5,
            'Milho': 5.0,
            'Palma Forrageira': 2.0,
            'Mandioca': 3.0
        }.get(cultura, 3.0)

        volume = round(evapo * demanda_base * fator_solo * 10, 2)  # litros por dia
        self.resultado.text = f"Volume ideal estimado: {volume} litros/dia"

    def ouvir_recomendacao(self, instance):
        texto = self.resultado.text
        if texto:
            falar("Resultado do simulador: " + texto)
        else:
            falar("Preencha os campos e clique em calcular para ouvir a recomendação.")

    def voltar(self, instance):
        self.manager.current = 'home'
