//Include libraries
#include <Servo.h>

#include <DRV8833.h>

//create motor objects
DRV8833 driver = DRV8833();
Servo myservo;  

//define constants and variables
const int red=6, green=7, blue=8;
const int inputA1 = 5, inputA2 = 4, inputB1 = 12, inputB2 = 11;
const int servopin = 9;

const int motorSpeedslow = 140;
const int motorSpeedfast = 200;

bool ce= LOW;
bool bit1=LOW;
bool bit2=LOW;

bool bit3=LOW;


int flag=0;

//initialize pins
void setup() 
{
  Serial.begin(9600);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);

  pinMode(inputA1, OUTPUT);
  pinMode(inputA2, OUTPUT);
  pinMode(inputB1, OUTPUT);
  pinMode(inputB2, OUTPUT);
  
  pinMode(servopin, OUTPUT);

  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  
  
  while (!Serial);


  myservo.attach(servopin);  // attaches the servo on pin 9 to the servo object
  myservo.write(0); 
  
  
  delay(300);

    // Attach the motors to the input pins:
  driver.attachMotorA(inputA1, inputA2);
  driver.attachMotorB(inputB1, inputB2);
  
}

//process code
void loop() 
{
  
  ce = digitalRead(A1);
  Serial.println("CE: ");
  Serial.println(ce);
  
  if  (ce == HIGH)
  {
    bit1=digitalRead(A2);
    bit2=digitalRead(A3);
    bit3=digitalRead(A4);
    
    Serial.println("Bit1: ");
    Serial.println(bit1);
    Serial.println("Bit2: ");
    Serial.println(bit2);
    Serial.println("Bit3: ");
    Serial.println(bit3);
    

    //Happiness - done
    if(bit1==HIGH and bit2==LOW && bit3 == LOW){
      Serial.println("Happy");
      driver.motorBReverse(motorSpeedslow);
      driver.motorAForward(motorSpeedslow);
      digitalWrite(red,HIGH);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW);
      delay(1000);
      digitalWrite(red,LOW);
      digitalWrite(blue, HIGH);
      digitalWrite(green, LOW);
      delay(1000);
      digitalWrite(red,LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, HIGH);
      delay(3500);  

      driver.motorBStop();   
      driver.motorAStop();
         

      delay(1000);
      digitalWrite(red,LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW);
        
      Serial.println("Happy 1");
      
    }
    //Sadness - done
    if(bit1==LOW and bit2==HIGH && bit3 == LOW){
      Serial.println("Sad");
      digitalWrite(red,LOW);
      digitalWrite(blue, HIGH);
      digitalWrite(green, LOW);
      
    }

    //Fear - done
    if(bit1==HIGH and bit2==HIGH && bit3 == LOW)
    {
      Serial.println("Fear");
      digitalWrite(red,HIGH);
      digitalWrite(blue, HIGH);
      digitalWrite(green, LOW);
      //cover eyes with tentacles
      myservo.write(180); 
      // Put the motors in reverse using the speed:
      driver.motorAForward(motorSpeedslow);
      driver.motorBForward(motorSpeedslow);
      // Wait to see the effect:
      delay(500);
      //Stop
      driver.motorAStop();
      driver.motorBStop();
      //Forward
      delay(2000);
      myservo.write(0);
      driver.motorAReverse(motorSpeedslow);
      driver.motorBReverse(motorSpeedslow);
      delay(500);
      //Stop
      driver.motorAStop();
      driver.motorBStop();
      //uncover eyes
      
      delay(2000);
    }

    //Disgust - done
    if(bit1==LOW and bit2==LOW && bit3 == HIGH)
    {
      Serial.println("Disgust");
      digitalWrite(red,HIGH);
      digitalWrite(blue, HIGH);
      digitalWrite(green, LOW);




     
      if (flag == 0) {
        myservo.write(0);              // tell servo to go to position in variable 'pos'
        delay(400);                       // waits 15ms for the servo to reach the position
        myservo.write(180);              // tell servo to go to position in variable 'pos'
                               // wait for a second       
        delay(1100);                       // waits 15ms for the servo to reach the position
        flag=1;
        }
        
        for (int j=0; j<5;j++){
          myservo.write(0);              // tell servo to go to position in variable 'pos'
          delay(100);                       // waits 15ms for the servo to reach the position
          myservo.write(180);              // tell servo to go to position in variable 'pos'
          delay(100); 
        }
        myservo.write(180);              // tell servo to go to position in variable 'pos'
        delay(500);                       // waits 15ms for the servo to reach the position
        flag=1;
        
        for (int j=0; j<5;j++){
          myservo.write(0);              // tell servo to go to position in variable 'pos'
          delay(100);                       // waits 15ms for the servo to reach the position
          myservo.write(180);              // tell servo to go to position in variable 'pos'
          delay(100); 
        }
        myservo.write(0);

    }
    //Anger
    if(bit1==HIGH and bit2==LOW && bit3 == HIGH){
      Serial.println("Anger");
      digitalWrite(red,HIGH);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW);

      // Put the motors in reverse using the speed:
      driver.motorAReverse(motorSpeedslow);
      driver.motorBReverse(motorSpeedslow);
      // Wait to see the effect:
      delay(100);
      //Stop
      driver.motorAReverse(motorSpeedslow);
      driver.motorBStop();
      //Forward
      delay(200);
      driver.motorAReverse(motorSpeedslow);
      driver.motorBReverse(motorSpeedslow);
      delay(100);
      driver.motorAStop();
      driver.motorBReverse(motorSpeedslow);
      delay(200);

      driver.motorAStop();
      driver.motorBStop();
      


      // 8 path code


      /*
                 _ _
               /     \
              /       \
              \       /
               \ _ _ /    <- an 8
               /     \
              /       \
              \       /
               \ _ _ /
       
            
       */     
    }
  }
  else
  {
    digitalWrite(red,HIGH);
    digitalWrite(blue, HIGH);
    digitalWrite(green, HIGH);
  }
}

