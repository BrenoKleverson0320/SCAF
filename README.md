# SCAF - Sistema de Controle de Acesso Facial
Trabalho de Conclusão de Curso na Modalidade de Artigo Científico apresentado a Faculdade de Tecnologia do Amapá - META, como requisito final à obtenção do grau de Bacharel em Engenharia de Computação.

## Detalhes

- Data apresentação: 
- Nota obtida:

## Resumo

> Este projeto de desenvolvimento de um sistema de segurança integrado, apresentada pelo grupo da Faculdade Meta, objetivava unir esforços de diferentes setores para criar uma inteligência artificial capaz de identificar potenciais ameaças por meio do monitoramento de câmeras de segurança. Esta proposta não apenas foi concretizada, mas também se mostrou promissora nos testes preliminares, evidenciando a viabilidade e eficácia do projeto.

## Componentes do projeto

- Back-end, feito em **Python** com o Framework **Django**
    -Recebe fotos e armazena elas no dataset, onde são usadas para fazer o treinamento da inteligência artificial.
    - Possui uma interface **WEB** para permiti o cadastro de alunos e Funcionários, e uma opção para bloquear as pessoas.
    - Possibilita uma conexão direta com o arduino para fazer o controle de acesso através da tranca e emite um som quando detecta uma
pessoa Bloqueada.
## Bibliotecas utilizadas
- [TensorFlow](https://www.tensorflow.org/)
- [OpenCV](https://opencv.org/)
- [Pickle](https://docs.python.org/3/library/pickle.html)
- [Django](https://www.djangoproject.com/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [NumPy](https://numpy.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [Dlib](http://dlib.net/)
- [SQLite3](https://docs.python.org/3/library/sqlite3.html)
