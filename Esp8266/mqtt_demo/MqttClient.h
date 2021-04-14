#include "PubSubClient.h"

class MqttClient {
public:
  MqttClient(Client& cClient, const char* user, const char* password, const char* mqttServer, const char* id);

  void loop();

  void publish(const char* topicName, const char* data);

  void publish(const char* topicName, const char* data, const int len);

  void setCallback(MQTT_CALLBACK_SIGNATURE);

  bool isConnected() {
    return client.connected(); 
  }

  bool subscribe(const char* topic);

  bool subscribe(const char* topic, uint8_t qos);
private:
  void reconnect();
  
  PubSubClient client;

  const char* user;
  const char* password;
  const char* id;
};
