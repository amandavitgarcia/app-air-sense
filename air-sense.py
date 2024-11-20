#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

// Dados do WiFi
#define WIFI_SSID "SSID"
#define WIFI_PASSWORD "SENHA"
 
// Telegram BOT Token (Botfather)
#define BOT_TOKEN "TOKEN"

// Use @myidbot (IDBot) para saber qual o seu ID
#define CHAT_ID "0123"

WiFiClientSecure secured_client;
UniversalTelegramBot bot(BOT_TOKEN, secured_client);

#define MQ135_PIN A0  // Pino do sensor MQ-135
#define LIMITE_AR_RUIM 120  // Valor de limite para qualidade do ar ruim

bool flagArRuim = true;  // Controle para evitar mensagens repetidas

// Função para conectar ao WiFi
void conectarWiFi() {
  Serial.print("Conectando ao WiFi: ");
  Serial.println(WIFI_SSID);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  secured_client.setInsecure();  // Certificado seguro

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("\nWiFi conectado!");
  Serial.print("Endereço IP: ");
  Serial.println(WiFi.localIP());
}

// Função para enviar mensagem ao Telegram
void enviarMensagemTelegram(const String& mensagem) {
  if (WiFi.status() == WL_CONNECTED) {
    bool enviado = bot.sendMessage(CHAT_ID, mensagem, "");  // Envia mensagem
    if (enviado) {
      Serial.println("Mensagem enviada ao Telegram com sucesso.");
    } else {
      Serial.println("Erro ao enviar mensagem ao Telegram. Tentando novamente...");
      delay(1000);  // Aguarda antes de tentar novamente
      bot.sendMessage(CHAT_ID, mensagem, "");
    }
  } else {
    Serial.println("Erro: Sem conexão WiFi. Não foi possível enviar a mensagem.");
  }
}

// Função para verificar a qualidade do ar
void verificarQualidadeAr() {
  int valorSensor = analogRead(MQ135_PIN);  // Leitura do sensor MQ-135

  Serial.print("Valor do sensor MQ-135: ");
  Serial.println(valorSensor);

  if (valorSensor > LIMITE_AR_RUIM) {
    if (flagArRuim) {  // Envia mensagem apenas uma vez para cada mudança
      Serial.println("Alerta: Qualidade do ar ruim detectada!");
      enviarMensagemTelegram("⚠ Alerta: Qualidade do ar está ruim! Valor: " + String(valorSensor));
      flagArRuim = false;  // Bloqueia mensagens repetidas
    }
  } else {
    if (!flagArRuim) {  // Envia mensagem de normalização uma vez
      Serial.println("Qualidade do ar voltou ao normal.");
      enviarMensagemTelegram("✅ Qualidade do ar está boa novamente. Valor: " + String(valorSensor));
      flagArRuim = true;  // Permite novo envio se o ar piorar
    }
  }
}

void setup() {
  pinMode(MQ135_PIN, INPUT);  // Configura o pino do sensor como entrada

  Serial.begin(115200);
  Serial.println();

  // Conecta ao WiFi
  conectarWiFi();

  // Sincroniza o horário
  sincronizarTempo();

  // Envia mensagem inicial
  enviarMensagemTelegram("🤖 Bot iniciado! Monitorando a qualidade do ar...");
}

void loop() {
  verificarQualidadeAr();  // Verifica a qualidade do ar continuamente
  delay(1000);  // Aguarde 1 segundo antes de verificar novamente
}