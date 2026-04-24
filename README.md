# 🧠 Breast Cancer Image Analyzer

Sistema inteligente de apoio ao diagnóstico médico baseado em análise de imagens de ultrassom mamário.

---

## 📌 Sobre o projeto

Este projeto tem como objetivo auxiliar profissionais da saúde na detecção de câncer de mama por meio da análise automatizada de imagens de ultrassom. A solução utiliza técnicas de processamento de imagem e aprendizado profundo para identificar padrões associados a lesões benignas e malignas.

> ⚠️ **Importante:** Este sistema não substitui o diagnóstico médico. Ele atua como ferramenta de apoio à decisão clínica.

---

## 🚀 Funcionalidades

* Upload de imagens de ultrassom mamário
* Pré-processamento automático das imagens
* Extração de Região de Interesse (ROI)
* Classificação das imagens em:

  * Benigno
  * Maligno
  * Normal
* Exibição dos resultados com probabilidade associada
* Interface simples e intuitiva para uso clínico

---

## 🧪 Pipeline do modelo

O fluxo de processamento segue as seguintes etapas:

1. **Entrada de imagem**
2. **Pré-processamento**

   * Filtro guiado
   * Filtro de mediana
3. **Extração da ROI**
4. **Aumento de dados (Data Augmentation)**

   * Aplicado principalmente à classe benigna
5. **Classificação com ensemble de redes neurais**

   * EfficientNetB0
   * EfficientNetB1
   * EfficientNetB2
6. **Agregação dos resultados (Ensemble)**

---

## 🧠 Tecnologias utilizadas

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Scikit-learn
* Django / Django REST Framework
* React (ou React Native, se aplicável)

---

## 📊 Base de dados

* BUSI Dataset (Breast Ultrasound Images)

---

## 📷 Exemplo de uso

1. O médico realiza o upload da imagem de ultrassom
2. O sistema processa automaticamente a imagem
3. O resultado é exibido com a classificação e nível de confiança

---

## ⚙️ Como executar o projeto

### Backend

```bash
# Clone o repositório
git clone <repo-url>

# Acesse a pasta
cd backend

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
python manage.py runserver
```

### Frontend

```bash
cd frontend

npm install
npm start
```

---

## 📈 Resultados

O modelo apresentou bons resultados na classificação das imagens, especialmente com o uso de ensemble, reduzindo overfitting e aumentando a robustez das previsões.

*(Adicione aqui métricas como acurácia, precisão, recall e F1-score, se desejar)*

---

## ⚠️ Limitações

* Dependência da qualidade das imagens de entrada
* Possível viés na base de dados
* Não substitui avaliação clínica especializada

---

## 🔮 Trabalhos futuros

* Integração com sistemas hospitalares (PACS)
* Expansão para outros tipos de exames (mamografia, ressonância)
* Uso de modelos mais avançados (Vision Transformers)
* Explicabilidade dos modelos (Grad-CAM)

---

## 👨‍⚕️ Público-alvo

* Médicos radiologistas
* Clínicas de diagnóstico por imagem
* Pesquisadores na área de visão computacional aplicada à saúde

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 📬 Contato

Caso tenha dúvidas ou sugestões, entre em contato.

---
