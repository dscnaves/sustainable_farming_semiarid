# Sertão Sustentável

**Sertão Sustentável** é um aplicativo educacional e climático voltado para produtores do semiárido brasileiro. Ele oferece informações meteorológicas, hídricas e técnicas sustentáveis de cultivo, com foco em acessibilidade e uso offline.

---

## Objetivo

Promover o acesso à tecnologia e ao conhecimento ambiental para comunidades rurais, especialmente em regiões afetadas por:

- Seca prolongada  
- Baixa escolaridade  
- Dificuldades de infraestrutura  

---

## Funcionalidades Implementadas

| Tela                         | Finalidade                                                                 |
|------------------------------|----------------------------------------------------------------------------|
| Boas-Vindas                  | Introdução ao app com narração e imagem acolhedora                         |
| Home                         | Menu principal com acesso às funcionalidades                               |
| Localização                  | Permite digitar e salvar a cidade (ex: Campinas - SP, Brasil)              |
| Previsão do Tempo            | Exibe o clima atual com leitura por voz                                    |
| Previsão Climática           | Mostra tendências meteorológicas para os próximos dias                     |
| Balanço Hídrico              | Informa a umidade do solo e orientações de manejo                          |
| Boas Práticas                | Dicas de cultivo e irrigação sustentável                                    |
| Alertas Regionais            | Exibe riscos climáticos e ambientais relevantes para a região              |
| Biblioteca de Cultivos       | Lista de plantas adaptadas ao semiárido com descrição e leitura em voz     |
| Painel de Indicadores        | Mostra dados ambientais locais como temperatura, vento e precipitação      |
| Simulador de Irrigação       | Calcula volume ideal de água por tipo de cultura, solo e evapotranspiração |

---

## Acessibilidade

- Leitura em voz de todo o conteúdo com a biblioteca `pyttsx3`
- Botões com ícones visuais e texto claro
- Interface responsiva adaptada para telas simples

---

## Imagens Utilizadas

As imagens devem estar localizadas na pasta `images/`:

- `sertao_intro.png`
- `icone_megafone.png`
- `balanco_hidrico_solo.png`
- `cultivo_sustentavel.png`
- `icone_localizacao.png`
- `clima_variavel.png`
- `tempo_sol_nuvem.png`
- `icone_alerta.png`
- `icone_cultivo.png`
- `icone_indicadores.png`
- `icone_irrigacao.png`

---

## Requisitos

- Python 3.10 ou superior  
- [Kivy](https://kivy.org/) >= 2.3.1  
- `pyttsx3` (leitura em voz)  
- `plyer` (opcional para uso de GPS em Android)

### Instalação dos pacotes principais:

```bash
pip install kivy pyttsx3 plyer


## Execução

Certifique-se de que todas as imagens estejam na pasta correta e os arquivos `.py` estejam organizados conforme abaixo.  
Para iniciar a aplicação:

```bash
python main.py
```

## Estrutura sugerida do projeto

```
Projeto/
│
├── main.py
├── audio_util.py
├── localidade.txt
├── images/
│   └── [imagens utilizadas]
├── tela_boas_vindas.py
├── tela_localizacao.py
├── previsao_tempo.py
├── previsao_climatica.py
├── balanco_hidrico.py
├── boas_praticas.py
├── alertas_regionais.py
├── biblioteca_cultivos.py
├── painel_indicadores.py
└── simulador_irrigacao.py

```
