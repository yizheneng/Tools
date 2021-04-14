#include "MqttClient.h"
#include <functional>

MqttClient::MqttClient(Client& cClient, const char* user, const char* password, const char* mqttServer, const char* id)
  :client(cClient),
  id(id),
  user(user), 
  password(password)
{
  client.setServer(mqttServer, 1883);
}

void MqttClient::loop()
{
  while(1) {
    delay(5000);
    if (!client.connected()) {
      reconnect();
    } else {
      break;
    }
    client.loop();
  }
}

void MqttClient::publish(const char* topicName, const char* data)
{
  client.publish(topicName, data);
}

void MqttClient::publish(const char* topicName, const char* data, int len)
{
  client.publish(topicName, data, len);
}

bool MqttClient::subscribe(const char* topic)
{
  return client.subscribe(topic);
}

bool MqttClient::subscribe(const char* topic, uint8_t qos)
{
  return client.subscribe(topic, qos);
}

void MqttClient::setCallback(MQTT_CALLBACK_SIGNATURE)
{
  client.setCallback(callback);
}

void MqttClient::reconnect()
{
    Serial.println("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect(id, user, password)) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
    }
}
