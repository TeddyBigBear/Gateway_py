#include <U8x8lib.h>
#include <LoRa.h>
#include <WiFi.h>


// WIFI_LoRa_32 ports
// GPIO5  -- SX1278's SCK
// GPIO19 -- SX1278's MISO
// GPIO27 -- SX1278's MOSI
// GPIO18 -- SX1278's CS
// GPIO14 -- SX1278's RESET
// GPIO26 -- SX1278's IRQ(Interrupt Request)

#define SS      18
#define RST     14
#define DI0     26


// LoRa Settings 
#define BAND    866E6
#define spreadingFactor 7
#define SignalBandwidth 125E3
#define codingRateDenominator 5
#define preambleLength 8
#define syncWord 0x34

// the OLED used
U8X8_SSD1306_128X64_NONAME_SW_I2C u8x8(/* clock=*/ 15, /* data=*/ 4, /* reset=*/ 16);


// MAC adress
byte mac[6];
byte mac1[6]={0x01,0x01,0x01,0x01,0x01,0x01};
byte mac2[6]={0x02,0x02,0x02,0x02,0x02,0x02};


// emitter type
byte emitterType[3]={0x01,0x02,0x03};


// #################Packet test variable value for station meteo####################
// #################CONSTANTE HEADER####################
const byte bStation=0x42; // header battery voltage
const byte sStation=0x53; // header solar voltage
const byte tStation=0x54; // header temperation
const byte hStation=0x48; // header hydrometrie
const byte eStation=0x45; // header pluviometrie
const byte vStation=0x56; // header anemometre
const byte pStation=0x50; // header pression
const byte dStation=0x44; // header direction vent

// #################VARIABLE####################
byte errorFlagStation=0x00; 
byte batteryVoltageStation=0x00;
byte solarVoltageStation=0x00; 
byte temperatureStation[2]={0x00,0x00};
byte hydrometryStation=0x00;
byte pluviometryStation=0x00;
byte anemometryStation[2]={0x00,0x00};
byte pressureStation[2]={0x00,0x00};
byte windDirectionStation=0x00;

// #################Packet test variable value for rucher####################
// #################CONSTANTE HEADER####################
const byte bRucher=0x42; // header battery voltage
const byte mRucher=0x4D; // header T°masse
const byte tRucher=0x54; // header temperation
const byte hRucher=0x48; // header hydrometrie
const byte vRucher=0x56; // header vibration
const byte cRucher=0x43; // header CO2
const byte nRucher=0x4E; // header nour
const byte pRucher=0x50; // header masse


// #################VARIABLE####################
byte errorFlagRucher=0x00;
byte batteryVoltageRucher=0x00;
byte temperatureRucher[2]={0x00,0x00};
byte hydrometryRucher=0x00;
byte balanceRucher[2]={0x00,0x00};
byte vibrationRucher[2]={0x00,0x00};
byte co2Rucher[2]={0x00,0x00};
byte nourRucher=0x00;

//#################Variable de gestion du bouton d'envoie des messages####################

int counter=1, messageLostCounter = 0, messageNbr=0;
char str[5];
int lastButtonState = LOW;
const int senderButton = 37;
int buttonState;
long lastDebounceTime = 0;
long debounceDelay = 10000;

void setup() {
//#################Initialisation du port SPI avec le SX1276####################
  SPI.begin(5, 19, 27, 18); 
//#################Set des pins Slave select, reset et interupt####################
  LoRa.setPins(SS, RST, DI0);
//#################Initialisation du moniteur seriea 115000 bauds####################  
  Serial.begin(115200);
//#################Initialisation du wifi et recuperation de l'adresse MAC####################
  WiFi.begin();// Initialisation du wifi
  WiFi.macAddress(mac);
//#################Initialisation de l'afficheur OLED#################### 
  u8x8.begin(); //initialisation de l'ecran OLED
  u8x8.setFont(u8x8_font_chroma48medium8_r);
//#################if just the  basic function, must connect to a computer#################### 
  while (!Serial); 
  delay(1000);
//#################Initialiation du bouton d'envoi des message #################### 
  pinMode(senderButton, INPUT); 

  Serial.println("LoRa Sender");
  u8x8.drawString(0, 0, "LoRa Sender");
//#################Initialiation de la bibliotheque LoRa à la frequence 868Mhz #################### 
  if (!LoRa.begin(BAND)) { 
    Serial.println("Starting LoRa failed!");
    u8x8.drawString(0, 1, "Starting LoRa failed!");
    while (1);
  }
//#################Set du Spreading factor a 7, valeurs possible entre 6 et 12#################### 
  LoRa.setSpreadingFactor(spreadingFactor);
//#################Set de la bandwidth 125E3,valeur possible 7.8E3, 10.4E3, 15.6E3, 20.8E3, 31.25E3, 41.7E3, 62.5E3, 125E3, and 250E3 ####################  
  LoRa.setSignalBandwidth(SignalBandwidth);
 //#################Set du codingRate à 5,valeur possible entre 5 et 8 ####################   
  LoRa.setCodingRate4(codingRateDenominator);
 
  Serial.println("LoRa Initial OK!");
  Serial.print("LoRa Frequency: ");
  Serial.println(BAND);

  Serial.print("LoRa spreading Factor: ");
  Serial.println(spreadingFactor);
  
  Serial.print("LoRa bandwitdh: ");
  Serial.println(SignalBandwidth);
  
  
  Serial.print("MAC: ");
    Serial.print(mac[0],HEX);
    Serial.print(":");
    Serial.print(mac[1],HEX);
    Serial.print(":");
    Serial.print(mac[2],HEX);
    Serial.print(":");
    Serial.print(mac[3],HEX);
    Serial.print(":");
    Serial.print(mac[4],HEX);
    Serial.print(":");
    Serial.println(mac[5],HEX);

    u8x8.drawString(0, 1, "LoRa  OK!");
    u8x8.drawString(0, 1, "MAC:");
    u8x8.setCursor(4, 2);
    u8x8.print(mac[0],HEX);
    u8x8.setCursor(6, 2);
    u8x8.print(mac[1],HEX);
    u8x8.setCursor(8, 2);
    u8x8.print(mac[2],HEX); 
    u8x8.setCursor(10, 2);
    u8x8.print(mac[3],HEX); 
    u8x8.setCursor(12, 2);
    u8x8.print(mac[4],HEX);
    u8x8.setCursor(14, 2);
    u8x8.print(mac[5],HEX);
    delay(5000);
  
}

void loop() {
//C'est la boucle principale le programme est demarre lorqu'on appuie sur le boutton, le bouton est disponible uniquement toute les 10 secondes
//Lorsque le bouton est appuyé le message est envoyé
//Le programme attend un acknowledge du receveur le receveur verifie le message à l'aide du checksum et le renvoi à l'envoyeur
//Tant que le message n'est pas reçu parfaitement, l'emetteur renvoi le message tant que le receveur n'a pas confirmé le message
  int reading = digitalRead(senderButton);
  
  if (reading != lastButtonState) {
      lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
        if (reading != buttonState) {
            buttonState = reading;
            if (buttonState == HIGH) {
              sendMessageStr(createFrame(messageNbr));
              int nackCounter = 0;
              while (!receiveAck(createFrame(messageNbr)) && nackCounter <= 5) {
                Serial.println(" refused ");
                Serial.print(nackCounter);
                delay(1000);
                sendMessageStr(createFrame(messageNbr));
                nackCounter++;
              }
              if (nackCounter >= 5) {
                Serial.println("");
                Serial.println("--------------- MESSAGE LOST ---------------------");
                messageLostCounter++;
                delay(100);
              } 
              else {
                  Serial.println("Acknowledged ");
                  char str[5];
                  messageNbr++;
                  counter++;
                  if(messageNbr>3){
                    messageNbr=0;
                  }
                  Serial.println(" Sent pkt ");
                  Serial.print(counter);
                  u8x8.drawString(0, 5, "Sent pkt :");
                  itoa(counter,str,10);
                  u8x8.drawString(11, 3, str);
              }
          }
        }
    }
    lastButtonState = reading;
}
//###################Fonction qui envoi une chaine de caractere via le protocol LoRa###################
void sendMessageStr(String message) {
  Serial.print(message);
  // send packet
  LoRa.beginPacket();
  LoRa.print(message);
  LoRa.endPacket();
  delay(1000);
}
//###################Fonction acknowledge verifie que le message a été corectement transmit###################
bool receiveAck(String message) {
  String ack;
  Serial.print(" Waiting for Ack ");
  bool stat = false;
  unsigned long entry = millis();
  while (stat == false && millis() - entry < 2000) {
    if (LoRa.parsePacket()) {
      ack = "";
      while (LoRa.available()) {
        ack = ack + ((char)LoRa.read());
      }
      int check = 0;
      
      for (int i = 0; i < message.length(); i++) {
        check += message[i];
      }
      Serial.print(" Ack ");
      Serial.print(ack);
      Serial.print(" Check ");
      Serial.print(check);
      if (ack.toInt() == check) {
        Serial.print(" Checksum OK ");
        stat = true;
      }
    }
  }
  return stat;
}

//###################Fonction qui va génerer un message de trame simulation pour le LoRa###################
String createFrame(int frame)
{
   char message[90];
   if(frame==0)
   {
      sprintf(message,"%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh",emitterType[0],mac[0],mac[1],mac[2],mac[3],
      mac[4],mac[5],errorFlagStation,bStation,batteryVoltageStation,sStation,solarVoltageStation,tStation,temperatureStation[0],temperatureStation[1],hStation,
      hydrometryStation,eStation,pluviometryStation,vStation,anemometryStation[0],anemometryStation[1],pStation,pressureStation[0],pressureStation[1],dStation,windDirectionStation);
      
      return message;
   }
   else if (frame==1)
   {
      sprintf(message,"%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh%xhh",emitterType[1],mac1[0],
      mac1[1],mac1[2],mac1[3],mac1[4],mac1[5],emitterType[2],mac2[0],mac2[1],mac2[2],mac2[3],mac2[4],mac2[5]
      ,errorFlagRucher,bRucher,batteryVoltageRucher,mRucher,temperatureRucher[0],temperatureRucher[1],hRucher,
      hydrometryRucher,pRucher,balanceRucher[0],balanceRucher[1],vRucher,vibrationRucher[0],vibrationRucher[1],
      cRucher,co2Rucher[0],co2Rucher[1],nRucher,nourRucher);
      
      return message;
   }
   else if (frame==2)
   {
      //insert scenario here
      return message;
   }
   else
   {
      //insert scenario here
      return message;
   }
}



  

