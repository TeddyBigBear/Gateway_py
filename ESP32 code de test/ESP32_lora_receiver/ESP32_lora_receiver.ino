#include <U8x8lib.h>
#include <LoRa.h>

String receivedText;
String receivedRssi;
float receivedSnr;

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

void setup() {

  SPI.begin(5, 19, 27, 18);
  LoRa.setPins(SS, RST, DI0);

  Serial.begin(115200);
  while (!Serial); //if just the the basic function, must connect to a computer
  delay(1000);

  u8x8.begin();
  u8x8.setFont(u8x8_font_chroma48medium8_r);

  Serial.println("LoRa Receiver");
  u8x8.drawString(0, 1, "LoRa Receiver");

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

  u8x8.drawString(0, 1, "LoRa  OK!");
}

void loop() {

  // try to parse packet
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    // received a packet
    Serial.print("Received packet '");
    u8x8.drawString(0, 4, "PacketID");

    // read packet
    while (LoRa.available()) {
      receivedText = (char)LoRa.read();
      Serial.print(receivedText);
      char currentid[64];
      receivedText.toCharArray(currentid, 64);
      u8x8.drawString(9, 4, currentid);
    }

    // print RSSI of packet
    Serial.print("' with RSSI ");
    Serial.print(LoRa.packetRssi());
    u8x8.drawString(0, 5, "PacketRS");
    receivedRssi = LoRa.packetRssi();
    char currentrs[64];
    receivedRssi.toCharArray(currentrs, 64);
    u8x8.drawString(9, 5, currentrs);

     // print SNR of packet
    Serial.print(" with SNR ");
    Serial.println(LoRa.packetSnr());
    u8x8.drawString(0, 6, "PacketSNR");
    receivedSnr = LoRa.packetSnr();
    char currentsnr[64];
    dtostrf(receivedSnr,4,1,currentsnr);
    u8x8.drawString(10, 6, currentsnr);
  }

}
