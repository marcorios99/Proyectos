#define IO_USERNAME ""
#define IO_KEY ""
#define WIFI_SSID ""
#define WIFI_PASS ""
#include "AdafruitIO_WiFi.h"

AdafruitIO_WiFi io(IO_USERNAME, IO_KEY, WIFI_SSID, WIFI_PASS);
#define LED_PIN 16

AdafruitIO_Feed *slider = io.feed("Pregunta1_Tarea4");

void setup() {
 Serial.begin(115200);
 while(! Serial);
 Serial.print("Conectandose a Adafruit IO");
 io.connect();
 slider->onMessage(Mensaje_WEB);
 while(io.status() < AIO_CONNECTED) {
 Serial.print(".");
 delay(500);
 }

 Serial.println();
 Serial.println(io.statusText());
}

void loop() {
 io.run();
}
void Mensaje_WEB(AdafruitIO_Data *data) {
 int reading = data->toInt();
 Serial.print("Recibido <- ");
 Serial.println(reading);
 analogWrite(LED_PIN, reading);
}