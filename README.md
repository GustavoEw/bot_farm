# 🎮 Duel Links Auto Turn

Um script em **Python + OpenCV** criado para automatizar os duelos de personagens do **Yu-Gi-Oh! Duel Links**.

A ideia surgiu de um problema simples: **eu estava com preguiça de jogar manualmente os duelos de personagem**. Então criei um script capaz de identificar elementos específicos na tela, clicar neles automaticamente, passar os turnos até a derrota e, quando disponível, coletar as recompensas.

> ⚠️ **Projeto experimental/pessoal:** este projeto foi desenvolvido para automatizar uma tarefa repetitiva dentro do jogo. Use por sua conta e risco e esteja ciente das regras do jogo e da plataforma.

---

## 🧠 Como funciona?

O script utiliza **visão computacional** para procurar imagens pré-configuradas na tela do computador.

O funcionamento básico é:

1. Captura a tela utilizando `MSS`;
2. Procura pelas imagens existentes na pasta `ranked/`;
3. Utiliza o `OpenCV` para comparar as imagens com a tela;
4. Quando encontra uma correspondência acima do nível de confiança definido, calcula o centro da imagem;
5. Move o mouse até o local encontrado;
6. Realiza um clique automaticamente;
7. Continua verificando a tela até o usuário pressionar `Q`.

### Fluxo

```text
Capturar tela
      ↓
Procurar imagens na pasta "ranked"
      ↓
Encontrou alguma imagem?
      ↓
     Sim
      ↓
Calcular posição
      ↓
Mover mouse
      ↓
     Clicar
      ↓
Continuar monitorando
      ↓
Pressionar Q → Encerrar
```

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **OpenCV** — reconhecimento das imagens na tela
* **NumPy** — manipulação das imagens
* **MSS** — captura rápida da tela
* **PyAutoGUI** — movimentação e cliques do mouse
* **Keyboard** — identificação da tecla `Q`

---

## 📁 Estrutura do projeto

```text
Duel-Links-Auto-Turn/
│
├── ranked/
│   ├── imagem1.png
│   ├── imagem2.png
│   ├── imagem3.png
│   └── ...
│
├── main.py
├── requirements.txt
└── README.md
```

A pasta `ranked/` deve conter as imagens que o programa precisa encontrar durante o duelo.

---

## ⚙️ Requisitos

É necessário ter:

* Python 3.x
* Yu-Gi-Oh! Duel Links
* Windows
* Resolução configurada de acordo com as imagens utilizadas

Instale as dependências com:

```bash
pip install -r requirements.txt
```

Ou diretamente:

```bash
pip install opencv-python numpy mss pyautogui keyboard
```

---

## 🎮 Configuração do Duel Links

Antes de executar o script, algumas configurações são importantes.

### Configurações recomendadas

* **Resolução:** `1920x1080`
* **Configurações do duelo:** modo **Automático**
* Deixe o jogo em uma posição consistente na tela.

O reconhecimento é baseado em **comparação de imagens**. Por isso, a posição e o tamanho dos elementos na tela são importantes.

### ⚠️ Está usando outra resolução?

As imagens da pasta `ranked/` foram feitas considerando uma determinada resolução.

Se você estiver utilizando uma resolução diferente de **1920x1080**, será necessário **substituir as imagens da pasta `ranked/` por imagens capturadas na resolução do seu computador**.

Por exemplo:

```text
1920x1080
   ↓
imagens capturadas em 1920x1080
```

Se estiver usando:

```text
1366x768
```

as imagens utilizadas pelo script também devem ser capturadas nessa resolução.

---

## 🎯 Nível de confiança

O reconhecimento utiliza o seguinte valor:

```python
CONFIANCA = 0.85
```

Esse valor determina o quanto a imagem encontrada precisa ser semelhante ao modelo.

Quanto maior o valor:

* Menos falsos positivos;
* Maior exigência na correspondência da imagem.

Quanto menor:

* Pode reconhecer imagens semelhantes;
* Porém aumenta a possibilidade de clicar em locais incorretos.

Se estiver tendo problemas para reconhecer uma imagem, o valor pode ser ajustado.

---

## ▶️ Executando

Com o Duel Links aberto e configurado corretamente:

```bash
python main.py
```

O programa começará a monitorar a tela.

Quando uma das imagens da pasta `ranked/` for encontrada, o script realizará automaticamente o clique correspondente.

Para encerrar o programa:

```text
Pressione Q
```

O terminal exibirá:

```text
Programa encerrado.
```

---

## 🔍 Exemplo de reconhecimento

Quando uma imagem é encontrada, o programa mostra no terminal algo semelhante a:

```text
imagem.png encontrado (0.92)
```

O número representa o nível de confiança encontrado pelo `OpenCV`.

Por exemplo:

```text
imagem.png encontrado (0.92)
```

significa que a correspondência encontrada atingiu aproximadamente `92%` de similaridade.

---

## 🧩 Personalização

As principais configurações estão no início do código:

```python
PASTA_IMAGENS = "ranked"
CONFIANCA = 0.85
```

### Pasta das imagens

```python
PASTA_IMAGENS = "ranked"
```

Define onde o programa procura as imagens.

Você pode alterar para outra pasta:

```python
PASTA_IMAGENS = "imagens"
```

### Confiança

```python
CONFIANCA = 0.85
```

Define o nível mínimo de confiança para que uma imagem seja considerada encontrada.

---

## 💡 Por que esse projeto foi criado?

Este projeto começou como uma forma de resolver uma tarefa extremamente repetitiva.

Eu queria realizar os **duelos de personagem do Duel Links**, mas não queria ficar passando os turnos e repetindo os mesmos cliques manualmente.

Então surgiu a ideia:

> **"E se eu simplesmente ensinasse o computador onde clicar?"**

A partir disso, utilizei Python e OpenCV para criar um pequeno sistema de visão computacional capaz de reconhecer elementos da interface e interagir com eles.

Além de automatizar a tarefa, o projeto também serviu como uma forma prática de estudar:

* Visão computacional;
* Reconhecimento de padrões;
* Automação com Python;
* Manipulação de imagens;
* Captura de tela;
* Automação de mouse e teclado.

---

## 🚀 Possíveis melhorias

Algumas ideias para futuras versões:

* [ ] Adicionar suporte para diferentes resoluções automaticamente;
* [ ] Criar uma interface gráfica para configurar o programa;
* [ ] Permitir selecionar as imagens diretamente pela interface;
* [ ] Adicionar sistema de logs;
* [ ] Melhorar a velocidade do reconhecimento;
* [ ] Utilizar regiões específicas da tela para reduzir processamento;
* [ ] Adicionar configuração do nível de confiança;
* [ ] Criar um sistema para detectar automaticamente o fim do duelo;
* [ ] Adicionar suporte a diferentes layouts do jogo.

---

## ⚠️ Observações

Este projeto depende do reconhecimento visual da interface. Alterações no layout, escala da interface, resolução ou posição da janela podem fazer com que o reconhecimento deixe de funcionar corretamente.

**Não execute o script sem antes verificar se as imagens utilizadas correspondem à sua configuração de tela.**

Também é recomendado testar o programa inicialmente observando os cliques realizados, antes de deixá-lo funcionando sozinho.

---

## 👨‍💻 Autor

**Gustavo Ewerthon**

Estudante de **Sistemas de Informação**, interessado em desenvolvimento, automação, visão computacional e criação de soluções práticas utilizando programação.

Este projeto faz parte dos meus experimentos utilizando **Python e OpenCV para resolver problemas reais do meu dia a dia**.

---

## 📄 Licença

Este projeto é disponibilizado para fins educacionais e experimentais.

Consulte as regras e os termos de uso do jogo antes de utilizar qualquer forma de automação.
