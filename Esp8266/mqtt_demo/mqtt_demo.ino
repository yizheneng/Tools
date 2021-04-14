#include <ESP8266WiFi.h>
#include "MqttClient.h"

int led = D4;
const char username[] = "2OL9eyFM03";
const char password[] = "version=2018-10-31&res=products%2F2OL9eyFM03%2Fdevices%2Ffash&et=3537255523&method=md5&sign=rqSdag4EUmoXQ0CNWXWmKA%3D%3D";
const char id[] = "fash";
const char mqttServer[] = "218.201.45.7";
//const char mqttServer[] = "192.168.150.221";

WiFiClient espClient;
MqttClient mqttClient(espClient, username, password, mqttServer, id);

void callback(char* topic, uint8_t* dataP, unsigned int len)
{
  dataP[len] = '\0';
  Serial.printf("Topic %s, data:%s \r\n", topic, (char*)dataP);
}

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  WiFi.begin("Cnbot-Work", "Cnbot001");
  mqttClient.setCallback(callback);
}

char strBuffer[100];
void loop() {
  while(1) {
    if(WiFi.status() != WL_CONNECTED) {
      digitalWrite(led, !digitalRead(led));
      delay(100);
    } else {
      delay(1000);
      digitalWrite(led, !digitalRead(led)); 
      
      snprintf(strBuffer, 100, "led status:%d", digitalRead(led));
      uint8_t ledStatus = digitalRead(led);
      mqttClient.publish("LightStatus", (char*)&ledStatus, 1);
      mqttClient.subscribe("test");
      mqttClient.loop();
    }
  }
}
