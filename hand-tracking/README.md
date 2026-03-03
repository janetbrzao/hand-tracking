RECONHECIMENTO DE MÃOS COM PYTHON
Projeto de Visão computacional desenvolvido com Python para detecção e rastreamento de mãos em tempo real utilizando webcam. O sistema identifica landmarks da mão e realiza a contagem de dedos levantados.

FUNCIONALIDADES
- Detecção de até duas mãos simultaneamente
- Rastreamento de 21 pontos (landmarks) por mãos
- Contagem automática de dados levantados
- Exibição em tempo real pela webcam

TECNOLOGIAS UTILIZADAS
- Python
- OpenCV
- MediaPipe

COMO EXECUTAR O PROJETO
git clone https://github.com/janetbrzao/hand-tracking.git
cd hand-tracking

Instale as dependencias:
pip install -r requirements.txt

Execute o programa:
python app.py
ou
py app.py

Pressione ESC para encerrar.

CONCEITOS APLICADOS
- Computer Vision
- Processamento de imagem em tempo real
- Detecção de landmarks com MediaPipe
- Manipulação de frames com OpenCV

POSSIVEIS MELHORIAS FUTURAS
- Classificação de gestos especificos
- Reconhecimento de sinais da Libras
- Integração com modelo de Machine Learning

- Interface gráfica
