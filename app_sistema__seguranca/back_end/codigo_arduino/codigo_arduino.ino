
/*const int RelePin = 7; // Pino ao qual o Módulo Relé está conectado
const int BuzzerPin = 8; // Pino ao qual o buzzer está conectado

int incomingByte;      // Variável para ler dados recebidos pela serial
bool relayState = HIGH; // Estado inicial do relé (ligado)
bool soundOn = false;  // Estado do som
unsigned long lastRelayChangeTime = 0; // Momento da última mudança no relé

void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial em 9600bps
  pinMode(RelePin, OUTPUT); // Seta o pino do relé como saída
  pinMode(BuzzerPin, OUTPUT); // Seta o pino do buzzer como saída
  digitalWrite(RelePin, relayState); // Seta o pino do relé com o estado inicial
  digitalWrite(BuzzerPin, HIGH); // Seta o pino do buzzer com o estado inicial (ligado)
}

void loop() {
  if (Serial.available() > 0) {
    // Verifica se tem algum dado na serial
    incomingByte = Serial.read();  // Lê o primeiro dado do buffer da serial

    if (incomingByte >= '1') { // Se o comando for '1'
      // Aguarda 5 segundos
      //delay(5000);
      relayState = LOW; // Desliga o relé
      digitalWrite(RelePin, relayState); // Atualiza o pino do relé
      lastRelayChangeTime = millis(); // Armazena o momento da mudança do relé
      
      //soundOn = false; // Ativa o som
    } else if (incomingByte == '0') { // Se o comando for '0'
      relayState = !relayState; // Inverte o estado do relé
      digitalWrite(RelePin, relayState); // Atualiza o pino do relé
      //relayState = LOW; // Desliga o relé
      soundOn = false; // Desativar som


      
    } else if (incomingByte == '2') { // Se o comando for '2'
      relayState = LOW; // Desliga o relé
      digitalWrite(RelePin, relayState); // Atualiza o pino do relé
      soundOn = true; // ativar o som
    }
  }

  // Controla o som (buzzer)
  if (soundOn) {
    tone(BuzzerPin, 500); // Liga o buzzer em 1000Hz
  } else {
    noTone(BuzzerPin); // Desliga o buzzer
  }

  // Desliga o relé após 10 segundos quando o comando '1' é recebido
  if (incomingByte == '1' && relayState == LOW && millis() - lastRelayChangeTime >= 3000) {
    relayState = HIGH; // Liga o relé
    digitalWrite(RelePin, relayState); // Atualiza o pino do relé
  }}

*/


const int RelePin = 7;      // Pino ao qual o Módulo Relé está conectado
const int BuzzerPin = 8;    // Pino ao qual o buzzer está conectado


int incomingByte;      // Variável para ler dados recebidos pela serial
bool relayState = HIGH; // Estado inicial do relé (ligado)
bool soundOn = false;  // Estado do som
unsigned long lastRelayChangeTime = 0; // Momento da última mudança no relé
unsigned long lastCommandTime = 0;      // Momento da última recepção do comando '1'

void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial em 9600bps
  pinMode(RelePin, OUTPUT); // Seta o pino do relé como saída
  pinMode(BuzzerPin, OUTPUT); // Seta o pino do buzzer como saída
  digitalWrite(RelePin, relayState); // Seta o pino do relé com o estado inicial
  digitalWrite(BuzzerPin, HIGH); // Seta o pino do buzzer com o estado inicial (ligado)
}



void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();  // Lê o primeiro dado do buffer da serial

    if (incomingByte == '3') { // Se o comando for '3'
       relayState = HIGH; // Desativa o relé
       digitalWrite(RelePin, relayState); // Atualiza o pino do relé
      // Interrompe a execução da função que trata o comando '1'
      // (não faz nada e pula para a próxima iteração do loop)
    } else if (incomingByte == '1' && millis() - lastCommandTime >= 6000) {
      // Se o comando '1' for recebido e passaram-se pelo menos 6 segundos
      delay(5000);
      relayState = LOW;
      digitalWrite(RelePin, relayState);
      lastRelayChangeTime = millis();
      lastCommandTime = millis();
      //soundOn = false;
    } else if (incomingByte == '0') { // Se o comando for '0'
      relayState = !relayState; // Inverte o estado do relé
      digitalWrite(RelePin, relayState); // Atualiza o pino do relé
      //relayState = LOW; // Desliga o relé
      soundOn = false; // Desativar som
      
    } 
    }
  

  if (incomingByte == '2') { // Se o comando for '2'
      relayState = LOW; // Desliga o relé
      digitalWrite(RelePin, relayState); // Atualiza o pino do relé
      soundOn = true; // ativar o som

}
  
  // Controla o som (buzzer)
  if (soundOn) {
    tone(BuzzerPin, 500); // Liga o buzzer em 1000Hz
  } else {
    noTone(BuzzerPin); // Desliga o buzzer
  }

  // Desliga o relé após 10 segundos quando o comando '1' é recebido
  if (relayState == LOW && millis() - lastRelayChangeTime >= 3000) {
    relayState = HIGH; // Liga o relé
    digitalWrite(RelePin, relayState); // Atualiza o pino do relé
  }




}
