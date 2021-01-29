
char userInput;
int userDataPyTk[] = {0,0};

void setup(){
  Serial.begin(9600);                        
  pinMode(LED_BUILTIN, OUTPUT);
}

void getUserData(){

  String userDataUpdate;
  String delayString;
  String blinkCountString;
  String findDelimeter;
  int delimeterInt = 0;
  
  delay(2000); // Need to wait for pyserial send time 
  userDataUpdate = Serial.readString();
  
  findDelimeter = userDataUpdate.indexOf('-');
  delimeterInt = findDelimeter.toInt();
  
  delayString = userDataUpdate;
  delayString.remove(delimeterInt);
  
  blinkCountString = userDataUpdate;
  blinkCountString.remove(0,delimeterInt+1);
  
  userDataPyTk[0] = delayString.toInt();
  userDataPyTk[1] = blinkCountString.toInt();
  
} // getUserData Function

void loop(){

if(Serial.available()> 0){ 
    int delayTime = 0;
    int numBlinks = 0;
    
    userInput = Serial.read();               // read user input
      
      if(userInput == 'o'){                
        digitalWrite(LED_BUILTIN, HIGH); 
      }
      if(userInput == 'x'){
       digitalWrite(LED_BUILTIN, LOW);         
      }
      if(userInput == 'b'){
        getUserData();
        delayTime = userDataPyTk[0];
        numBlinks = userDataPyTk[1];
        
        for(int i =0;i<numBlinks;i++){
          digitalWrite(LED_BUILTIN,LOW);
          delay(delayTime);
          digitalWrite(LED_BUILTIN,HIGH);
          delay(delayTime);
         }// Blink for loop
      digitalWrite(LED_BUILTIN, LOW); 
      }
  } // Serial.available
} // Void Loop

  
