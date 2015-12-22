
#include <OneWire.h>
#include <DallasTemperature.h>
 
OneWire oneWire(10);

DallasTemperature sensors(&oneWire);

float tempC;
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  sensors.setResolution(9);
  sensors.begin();
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(8, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(100);              // wait for a second
  digitalWrite(8, LOW);    // turn the LED off by making the voltage LOW
  
  sensors.requestTemperatures(); // Send the command to get temperatures
  Serial.print("Temperature for Device 1 is: ");
  Serial.println(sensors.getTempCByIndex(0)); // Why "byIndex"? 
  delay(100);
}
