#define BLYNK_TEMPLATE_ID ""
#define BLYNK_DEVICE_NAME "Multímetro"
#define BLYNK_AUTH_TOKEN ""

#define BLYNK_FIRMWARE_VERSION "0.1.0"
#define BLYNK_PRINT Serial
#define APP_DEBUG

#define Pin_Voltaje V4
#define Pin_Corriente V5

//Your WiFi Credentials
char auth[] = "";
char ssid[] = "";
char pass[] = "";

//------------------------------

#define BLYNK_PRINT Serial
#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <Adafruit_GFX.h>

#include "RTClib.h"
#include <Wire.h>

#include "SD.h"
#include "SPI.h"

//Puertos
const int puertoVoltaje = 34;
const int puertoVoltaje_2 = 32;

//Variables
int Voltaje_leido = 0;
int Voltaje_leido_2 = 0;
float vout = 0.0;
float vout_2 = 0.0;
float vin_1 = 0.0;
float vin_2 = 0.0;
float current = 0.0;
const int CSpin = 2;
File sensorData;

float R1 = 100000;  //Resistencia 1
float R2 = 15;      //Resistencia 2
float R3 = 10000;   //Resistencia 3

char daysOfTheWeek[7][12] = {"Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"};

String $vin_1 = "0";
String $vin_2 = "0";
String data ="";

RTC_DS3231 rtc;

void setup() {
  // put your setup code here, to run once:
  Blynk.begin(auth, ssid, pass);
  Serial.begin(115200);
  delay(1000);
  pinMode(puertoVoltaje,INPUT_PULLUP);
  pinMode(puertoVoltaje_2,INPUT_PULLUP);
  if(!rtc.begin()){
    Serial.println("No se pudo encontrar RTC");
    while(1);    
  }
  rtc.adjust(DateTime(__DATE__, __TIME__));

  Serial.println("Initializing SD card...");
   if (!SD.begin(CSpin)) {
    Serial.println("Card failed, or not present");
    return;
   }
   Serial.println("card initialized."); 

}

void guardaDatoCSV(float voltaje, float corriente, DateTime now){
  data = String(voltaje) + ";" + String(corriente)+";"+String(now.hour())+":"+String(now.minute());
  sensorData = SD.open("/data.csv", FILE_APPEND);
  if (sensorData){
  sensorData.println(data);
  sensorData.close(); // close the file
  Serial.println("DATO GUARDADO EXITOSAMENTE");
}
else{
  Serial.println("Problema");
}
}

void loop() {
  
  // put your main code here, to run repeatedly:
  DateTime now = rtc.now();
  Voltaje_leido = analogRead(puertoVoltaje);
  vout = (Voltaje_leido * 5)/4095.0;
  vin_1 = vout/((R2+R3)/(R1+R2+R3));
  $vin_1 = String(vin_1);
  Serial.print("Voltaje V1 = ");
  Serial.println(vin_1,3);

  Voltaje_leido_2 = analogRead(puertoVoltaje_2);  
  vout_2 = (Voltaje_leido_2 * 5)/4095.0;
  vin_2 = vout_2/(R3/(R1+R2+R3));
  //$vin_2 = String(vin_2);
  
  current = (vin_1-vin_2)/R2;

  //Serial.print("Voltaje V2 = ");
  //Serial.println(vin_2,3);

  Serial.print("Corriente = ");
  Serial.println(current,3);
  Blynk.virtualWrite(V4, vin_1);
  Blynk.virtualWrite(V5, current);
  Blynk.run();
  guardaDatoCSV(vin_1,current,now); 
  delay(3000);

  
  Serial.print("Hora: ");
  Serial.print(now.hour());  
  Serial.print(":");
  Serial.print(now.minute());  
  Serial.print(" - ");
  Serial.print(daysOfTheWeek[now.dayOfTheWeek()]);  
  Serial.print(" "); 
  Serial.print(now.day());
  Serial.print("/"); 
  Serial.print(now.month());
  Serial.print("/"); 
  Serial.println(now.year());
}
