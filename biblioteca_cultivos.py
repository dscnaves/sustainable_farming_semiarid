from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from audio_util import falar

class BibliotecaCultivosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Título da tela
        layout.add_widget(Label(text='Biblioteca de Cultivos Adaptados', font_size=26))

        # Imagem de cabeçalho
        layout.add_widget(Image(source='images/icone_cultivo.png', size_hint_y=None, height=140))

        # Scroll com conteúdo das plantas
        scroll = ScrollView()
        grade = GridLayout(cols=1, spacing=12, size_hint_y=None)
        grade.bind(minimum_height=grade.setter('height'))

        cultivos = [
            {
                'nome': 'Feijão-de-corda',
                'detalhes': 'Ciclo curto, alta resistência à seca, ideal para rotação de culturas.'
            },
            {
                'nome': 'Milheto',
                'detalhes': 'Grão tolerante à estiagem, excelente para cobertura do solo.'
            },
            {
                'nome': 'Sorgo',
                'detalhes': 'Usado para alimentação animal; demanda hídrica moderada.'
            },
            {
                'nome': 'Umbu',
                'detalhes': 'Fruta nativa resistente, usada para doces, sucos e agroindústria.'
            },
            {
                'nome': 'Palma forrageira',
                'detalhes': 'Fonte de água e alimento para rebanho em regiões áridas.'
            },
            {
                'nome': 'Mandioca',
                'detalhes': 'Raiz de fácil cultivo, alta produtividade mesmo com pouca chuva.'
            }
        ]

        for item in cultivos:
            bloco = BoxLayout(orientation='vertical', padding=5, size_hint_y=None, height=100)
            nome = Label(text=f"[b]{item['nome']}[/b]", markup=True, font_size=20)
            detalhes = Label(text=item['detalhes'], font_size=16)
            bloco.add_widget(nome)
            bloco.add_widget(detalhes)
            grade.add_widget(bloco)

        scroll.add_widget(grade)
        layout.add_widget(scroll)

        layout.add_widget(Button(
            text='Ouvir Dicas de Cultivos',
            size_hint_y=None,
            height=50,
            on_press=self.ouvirCultivos
        ))


        # Botão para retornar
        layout.add_widget(Button(
            text='Voltar à Tela Inicial',
            size_hint_y=None,
            height=50,
            on_press=self.voltar
        ))

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'home'

    def ouvirCultivos(self, instance):
        texto = (
            "Alguns cultivos adaptados ao semiárido incluem: feijão-de-corda, milheto, sorgo, umbu, palma forrageira e mandioca. "
            "Eles são resistentes à seca, têm baixa demanda hídrica e servem tanto para alimentação quanto para cobertura do solo. "
            "Use essas opções para aumentar a sustentabilidade da sua produção."
        )
        falar(texto)
