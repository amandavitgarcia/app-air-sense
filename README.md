# Projeto AirSense: Monitoramento Inteligente da Qualidade do Ar  com NodeMCU ESP8266 🌍

Feito por: 
Amanda Vitoria Garcia - 10290199
Ewellyn Millena dos Santos - 10408024

Este projeto foi criado para a matéria de Objetos Inteligentes Conectados da Universidade Presbiteriana Mackenzie que implementa um sistema de monitoramento da qualidade do ar usando um **NodeMCU ESP8266** e o sensor **MQ-135**. 
O sistema coleta dados em tempo real e envia notificações automáticas para o Telegram quando os níveis de qualidade do ar ultrapassam limites configurados.

---

## 🛠️ **Funcionalidades**
- Conexão automática à rede WiFi.
- Medição contínua da qualidade do ar usando o sensor MQ-135.
- Notificação via Telegram:
  - **Alerta:** Quando os níveis de qualidade do ar ultrapassam o limite de segurança.
  - **Atualização:** Quando os níveis voltam ao normal.
- Configuração de limites ajustáveis para segurança ambiental.

---

## 🧰 **Tecnologias e Ferramentas Utilizadas**
- **Hardware**:
  - NodeMCU ESP8266
  - Sensor MQ-135
- **Linguagem**:
  - Python (Arduino)
- **Integrações**:
  - Telegram Bot API

---

## 🚀 **Como Executar**
### Pré-requisitos
- **Arduino IDE** instalado.
- Biblioteca **ESP8266WiFi** e **UniversalTelegramBot** configuradas na Arduino IDE.
- Credenciais de uma rede WiFi (SSID e senha).
- Token de um bot Telegram (criado via BotFather).
