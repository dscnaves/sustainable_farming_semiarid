from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Importa telas personalizadas
from tela_boas_vindas import TelaBoasVindas
from previsao_tempo import PrevisaoTempoScreen
from previsao_climatica import PrevisaoClimaticaScreen
from balanco_hidrico import BalancoHidricoScreen
from boas_praticas import BoasPraticasScreen
from tela_localizacao import TelaLocalizacao
from alertas_regionais import AlertasRegionaisScreen
from biblioteca_cultivos import BibliotecaCultivosScreen
from painel_indicadores import PainelIndicadoresScreen
from simulador_irrigacao import SimuladorIrrigacaoScreen

# Telas base
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Label(text='Sertão Sustentável', font_size=32))
        layout.add_widget(Button(text='Inserir Localização', on_press=self.goto_localizacao))
        layout.add_widget(Button(text='Previsão do Tempo', on_press=self.goto_previsao))
        layout.add_widget(Button(text='Previsão Climática', on_press=self.goto_climatica))
        layout.add_widget(Button(text='Balanço Hídrico', on_press=self.goto_balanco))
        layout.add_widget(Button(text='Boas Práticas', on_press=self.goto_boaspraticas))
        layout.add_widget(Button(text='Alertas Regionais', on_press=self.goto_alertas))
        layout.add_widget(Button(text='Biblioteca de Cultivos', on_press=self.goto_cultivos))
        layout.add_widget(Button(text='Painel Ambiental', on_press=self.goto_indicadores))       
        layout.add_widget(Button(text='Simulador de Irrigação', on_press=self.goto_irrigacao))
        self.add_widget(layout)

    def goto_localizacao(self, instance):
        self.manager.current = 'localizacao'

    def goto_previsao(self, instance):
        self.manager.current = 'tempo'

    def goto_climatica(self, instance):
        self.manager.current = 'climatica'

    def goto_balanco(self, instance):
        self.manager.current = 'balanco'

    def goto_boaspraticas(self, instance):
        self.manager.current = 'boaspraticas'

    def goto_alertas(self, instance):
        self.manager.current = 'alertas'
    
    def goto_cultivos(self, instance):
        self.manager.current = 'cultivos'

    def goto_indicadores(self, instance):
        self.manager.current = 'indicadores'

    def goto_irrigacao(self, instance):
        self.manager.current = 'irrigacao'

class LocalizacaoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Sua Localização'))
        layout.add_widget(Button(text='Voltar', on_press=self.voltar))
        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'home'

# App principal
class SertaoApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(TelaBoasVindas(name='inicio'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(TelaLocalizacao(name='localizacao'))
        sm.add_widget(PrevisaoTempoScreen(name='tempo'))
        sm.add_widget(PrevisaoClimaticaScreen(name='climatica'))
        sm.add_widget(BalancoHidricoScreen(name='balanco'))
        sm.add_widget(BoasPraticasScreen(name='boaspraticas'))
        sm.add_widget(AlertasRegionaisScreen(name='alertas'))
        sm.add_widget(BibliotecaCultivosScreen(name='cultivos'))
        sm.add_widget(PainelIndicadoresScreen(name='indicadores'))
        sm.add_widget(SimuladorIrrigacaoScreen(name='irrigacao'))

        sm.current = 'inicio'  # Começa pela tela de boas-vindas
        return sm

if __name__ == '__main__':
    SertaoApp().run()
