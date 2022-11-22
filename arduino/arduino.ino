#include <Keypad.h>

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns

char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};

byte rowPins[ROWS] = {2,3,4,5}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {8, 7, 6}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

const int ledCount = 10;   // the number of LEDs in the bar graph

int ledPins[] = {
  9,10,11,12,13,14,15,16,17,18
};  // an array of pin numbers to which LEDs are attached
int ledOn = 0;
String data;

void setup() {
  // loop over the pin array and set them all to output:
  for (int thisLed = 0; thisLed < ledCount; thisLed++) {
    pinMode(ledPins[thisLed], OUTPUT);
    digitalWrite(ledPins[thisLed], HIGH);
  }
  for(int thisLed = 0; thisLed < ledOn; thisLed++){
    digitalWrite(ledPins[thisLed], LOW);
    delay(300);
  }
  Serial.begin(9600);
  
}

void loop() {
  char key = keypad.getKey();
  if (key){
    Serial.println(key);
  }
    if (Serial.available() > 0) {
    data = Serial.readString();
    updateLedBar(data.toInt());
  }
}

void updateLedBar(int value){
  int ledOn = value / 10;
    for (int thisLed = 0; thisLed < ledCount; thisLed++) {
    pinMode(ledPins[thisLed], OUTPUT);
    digitalWrite(ledPins[thisLed], HIGH);
  }
  for(int thisLed = 0; thisLed < ledOn; thisLed++){
    digitalWrite(ledPins[thisLed], LOW);
    delay(30);
  }
}