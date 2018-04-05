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

// MAC adress
byte mac[6];

// the OLED used
U8X8_SSD1306_128X64_NONAME_SW_I2C u8x8(/* clock=*/ 15, /* data=*/ 4, /* reset=*/ 16);

int counter = 0;
char str[5];
int lastButtonState = LOW;
int senderButton = 37;
int buttonState;
long lastDebounceTime = 0;
long debounceDelay = 100;

void setup() {

  SPI.begin(5, 19, 27, 18);
  LoRa.setPins(SS, RST, DI0);
  WiFi.begin();
  WiFi.macAddress(mac);
  Serial.begin(115200);
  while (!Serial); //if just the the basic function, must connect to a computer
  delay(1000);
  
  pinMode(senderButton, INPUT);

  u8x8.begin();
  u8x8.setFont(u8x8_font_chroma48medium8_r);

  Serial.println("LoRa Sender");
  u8x8.drawString(0, 0, "LoRa Sender");

  if (!LoRa.begin(BAND)) {
    Serial.println("Starting LoRa failed!");
    u8x8.drawString(0, 1, "Starting LoRa failed!");
    while (1);
  }
  Serial.println("LoRa Initial OK!");
  
  Serial.print("LoRa Frequency: ");
  Serial.println(BAND);

  Serial.print("LoRa spreading Factor: ");
  Serial.println(spreadingFactor);
  LoRa.setSpreadingFactor(spreadingFactor);

  Serial.print("LoRa bandwitdh: ");
  Serial.println(SignalBandwidth);
  LoRa.setSignalBandwidth(SignalBandwidth);

  LoRa.setCodingRate4(codingRateDenominator);

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
    
    u8x8.setCursor(0, 2);
    u8x8.print(mac[0],HEX);
    
    u8x8.setCursor(2, 2);
    u8x8.print(mac[1],HEX);

    u8x8.setCursor(4, 2);
    u8x8.print(mac[2],HEX);
    
    u8x8.setCursor(6, 2);
    u8x8.print(mac[3],HEX);
    
    u8x8.setCursor(8, 2);
    u8x8.print(mac[4],HEX);
    
    u8x8.setCursor(10, 2);
    u8x8.print(mac[5],HEX);
    
  
  
  delay(5000);
  
}

void loop() {

  int reading = digitalRead(senderButton);
  if (reading != lastButtonState) {
      lastDebounceTime = millis();
  }
  
  
  if ((millis() - lastDebounceTime) > debounceDelay) {

      if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == HIGH) {
        // send packet
        LoRa.beginPacket();
        LoRa.print("025EFF56A2AFFF035EFF56A2AF1501B66T2805H24M10V90C1111N01P12");
        LoRa.endPacket();
        counter++;
        
        Serial.print("Sending packet: ");
        Serial.println(counter);
        Serial.println("data sent");
        u8x8.drawString(0, 3, "Sending pkt");
        itoa(counter,str,10);
        u8x8.drawString(13, 3, str);
      }
    }
  }
    lastButtonState = reading;
}
  

