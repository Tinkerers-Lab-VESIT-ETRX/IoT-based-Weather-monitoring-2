#include "DHT.h"
#define dht_1 2
#define DHTTYPE DHT11
DHT dht(dht_1,DHTTYPE);
void setup()
{
  Serial.begin (9600);
  pinMode(3,INPUT);
  dht.begin();
}

void loop() 
{
  float temp = dht.readTemperature();
  float humid = dht.readHumidity();
  int rain = digitalRead(3);
  int ldr=analogRead(A1);
  int air=analogRead(A0);
  Serial.println("T ="+ String(temp)+", H ="+String(humid)+", R ="+String(rain)+", L ="+String(ldr)+", A ="+String(air));
  delay (1000);
}

  
