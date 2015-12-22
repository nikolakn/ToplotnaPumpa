

const int senzor2k7 = A0;
const int senzor5k_1 = A1;
const int senzor5k_2 = A2;
const int senzor5k_3 = A3;
const int senzor5k_4 = A4;
const int senzor200k = A5;

int sensorValue = 0; 
long pauza1 = 0;
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
String senzorString = "";

#include <math.h>

double Thermistor2k7(int RawADC) {
 double Temp;
 double V = (5.0/1024.0)*RawADC;
 Temp = (13.5/V) - 2.7; 
 Temp = -25.9*log(Temp)+50.91;
 return Temp;
}
double Thermistor5k(int RawADC) {
 double Temp;
 double V = (5.0/1024.0)*RawADC;
 Temp = (25.5/V) - 5.1; 
 double A=1.28463e-3;
 double B=0.23625e-3;
 double C=9.2697e-8;
 double W = log(Temp*1000.0);
 Temp = 1.0/(A+W*(B+C*W*W))-273.15;
 return Temp;
}
/*
 double Thermistor5k(int RawADC) {
 double Temp;
 double V = (5.0/1024.0)*RawADC;
 Temp = (25.5/V) - 5.1; 
 Temp = -22.0*log(Temp)+64.71;
 return Temp-5;
}
 */
double Thermistor200k(int RawADC) {
 double Temp;
 double V = (5.0/1024.0)*RawADC;
 Temp = (1085.5/V) - 217.0; 
 Temp = -35.1*log(Temp)+198.5;
 return Temp+12;
}

void otvara(){
   digitalWrite(9, HIGH); 
   digitalWrite(10, LOW); 
   digitalWrite(11, LOW); 
   digitalWrite(12, HIGH); 
   delay(10); 
   digitalWrite(9, LOW); 
   digitalWrite(10, LOW); 
   digitalWrite(11, LOW); 
   digitalWrite(12, HIGH); 
   delay(10); 
   digitalWrite(9, LOW); 
   digitalWrite(10, LOW); 
   digitalWrite(11, HIGH); 
   digitalWrite(12, HIGH);
   delay(10);  
   digitalWrite(9, LOW); 
   digitalWrite(10, LOW); 
   digitalWrite(11, HIGH); 
   digitalWrite(12, LOW); 
   delay(10); 
   digitalWrite(9, LOW); 
   digitalWrite(10, HIGH); 
   digitalWrite(11, HIGH); 
   digitalWrite(12, LOW); 
   delay(10); 
   digitalWrite(9, LOW); 
   digitalWrite(10, HIGH); 
   digitalWrite(11, LOW); 
   digitalWrite(12, LOW); 
   delay(10); 
   digitalWrite(9, HIGH); 
   digitalWrite(10, HIGH); 
   digitalWrite(11, LOW); 
   digitalWrite(12, LOW);
   delay(10);
   digitalWrite(9, HIGH); 
   digitalWrite(10, LOW); 
   digitalWrite(11, LOW); 
   digitalWrite(12, LOW);
   delay(10);
}
void zatvara(){
   digitalWrite(9, HIGH); 
   digitalWrite(10, LOW); 
   digitalWrite(11, LOW); 
   digitalWrite(12, LOW);
   delay(10);
   digitalWrite(9, HIGH); 
   digitalWrite(10, HIGH); 
   digitalWrite(11, LOW); 
   digitalWrite(12, LOW);
   delay(10);
   digitalWrite(9, LOW); 
   digitalWrite(10, HIGH); 
   digitalWrite(11, LOW); 
   digitalWrite(12, LOW); 
   delay(10);  
   digitalWrite(9, LOW); 
   digitalWrite(10, HIGH); 
   digitalWrite(11, HIGH); 
   digitalWrite(12, LOW); 
   delay(10); 
   digitalWrite(9, LOW); 
   digitalWrite(10, LOW); 
   digitalWrite(11, HIGH); 
   digitalWrite(12, LOW); 
   delay(10); 
   digitalWrite(9, LOW); 
   digitalWrite(10, LOW); 
   digitalWrite(11, HIGH); 
   digitalWrite(12, HIGH);
   delay(10);  
   digitalWrite(9, LOW); 
   digitalWrite(10, LOW); 
   digitalWrite(11, LOW); 
   digitalWrite(12, HIGH); 
   delay(10); 
   digitalWrite(9, HIGH); 
   digitalWrite(10, LOW); 
   digitalWrite(11, LOW); 
   digitalWrite(12, HIGH); 
   delay(10); 
}

void setup() {
  // put your setup code here, to run once:
    // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);

  //step
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);

}
void read(){
  Serial.print("START;S2k7=");
  sensorValue =Thermistor2k7(analogRead(senzor2k7));
  Serial.print(sensorValue);
  //delay(5);
  Serial.print(";S5k_1=");
  sensorValue = Thermistor5k(analogRead(senzor5k_1));
  Serial.print(sensorValue);
  //delay(5);
  Serial.print(";S5k_2=");
  sensorValue = Thermistor5k(analogRead(senzor5k_2));
  Serial.print(sensorValue);
  //delay(5);
  Serial.print(";S5k_3=");
  sensorValue = Thermistor5k(analogRead(senzor5k_3));
  Serial.print(sensorValue);
  //delay(5);
  Serial.print(";S5k_4=");
  sensorValue = Thermistor5k(analogRead(senzor5k_4));
  Serial.print(sensorValue);
  //delay(5);
  Serial.print(";S200k=");
  sensorValue = Thermistor200k(analogRead(senzor200k));
  Serial.print(sensorValue);  
  Serial.println(";END"); 
}

void loop() {
  pauza1++;
  if(pauza1==20000){
    pauza1=0;
    read();
  }
  
  serialEvent(); //call the function
  // print the string when a newline arrives:
  if (stringComplete) {
    //Serial.println(inputString);
    if(inputString=="r1on\n"){
      digitalWrite(2, HIGH);  
    }
    if(inputString=="r1off\n"){
      digitalWrite(2, LOW);  
    }
    if(inputString=="r2on\n"){
      digitalWrite(3, HIGH);  
    }
    if(inputString=="r2off\n"){
      digitalWrite(3, LOW);  
    }
    if(inputString=="r3on\n"){
      digitalWrite(4, HIGH);  
    }
    if(inputString=="r3off\n"){
      digitalWrite(4, LOW);  
    }
    if(inputString=="r4on\n"){
      digitalWrite(5, HIGH);  
    }
    if(inputString=="r4off\n"){
      digitalWrite(5, LOW);  
    }
    if(inputString=="r5on\n"){
      digitalWrite(6, HIGH);  
    }
    if(inputString=="r5off\n"){
      digitalWrite(6, LOW);  
    }
    if(inputString=="r6on\n"){
      digitalWrite(7, HIGH);  
    }
    if(inputString=="r6off\n"){
      digitalWrite(7, LOW);  
    }
    
    if(inputString=="stepotvori\n"){
          for(int n=0; n<70;n++)
            otvara();  
    }
    if(inputString=="stepzatvori\n"){
          for(int n=0; n<70;n++)
            zatvara();  
    }
    if(inputString.substring(0,10)=="stepnapred"){
          int i = inputString.substring(10,12).toInt();
          for(int n=0; n<i;n++)
            otvara();  
    }    
    if(inputString.substring(0,9)=="stepnazad"){
          int i = inputString.substring(9,11).toInt();
          for(int n=0; n<i;n++)
            zatvara();  
    }    
    if(inputString=="allon\n"){
      digitalWrite(2, HIGH); 
      digitalWrite(3, HIGH); 
      digitalWrite(4, HIGH);
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
    }
    if(inputString=="alloff\n"){
      digitalWrite(2, LOW); 
      digitalWrite(3, LOW); 
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(7, LOW); 
    }
    
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
