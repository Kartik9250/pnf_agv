#include <ros.h>
#include <pnf_agv/Motor_desc.h>
#include <pnf_agv/Motor_driver.h>
#include <pnf_agv/Holo_agv.h>
ros::NodeHandle nh;

const int freq = 5000;
const int ledChannel1 = 0;
const int ledChannel2 = 1;
const int ledChannel3 = 2;
const int ledChannel4 = 3;
const int resolution = 8;

const int MD1_STBY=13;
const int MD2_STBY=15;

const int FR_PWM=33;
const int FR_AIN1=22;
const int FR_AIN2=23;

const int FL_PWM=27;
const int FL_BIN1=14;
const int FL_BIN2=12;

const int BR_PWM=21;
const int BR_AIN1=19;
const int BR_AIN2=18;

const int BL_PWM=16;
const int BL_BIN1=4;
const int BL_BIN2=0;






void motorCb(const pnf_agv::Holo_agv& msg){
//  digitalWrite(MD1_STBY, HIGH);
//  digitalWrite(MD2_STBY, msg.motor_driver_back.stby);

  digitalWrite(FR_AIN1, msg.motor_driver_front.motor_right.IN1);
  digitalWrite(FR_AIN2, msg.motor_driver_front.motor_right.IN2);
  // digitalWrite(FR_PWM, msg.motor_driver_front.motor_right.pwm);
  ledcWrite(ledChannel1, msg.motor_driver_front.motor_right.pwm);
  
  digitalWrite(FL_BIN1, msg.motor_driver_front.motor_left.IN1);
  digitalWrite(FL_BIN2, msg.motor_driver_front.motor_left.IN2);
  // digitalWrite(FL_PWM, msg.motor_driver_front.motor_right.pwm);
  ledcWrite(ledChannel2, msg.motor_driver_front.motor_left.pwm);
  
  digitalWrite(BR_AIN1, msg.motor_driver_back.motor_right.IN1);
  digitalWrite(BR_AIN2, msg.motor_driver_back.motor_right.IN2);
  // digitalWrite(BR_PWM, msg.motor_driver_front.motor_right.pwm);
  ledcWrite(ledChannel3, msg.motor_driver_back.motor_right.pwm);
  
  digitalWrite(BL_BIN1, msg.motor_driver_back.motor_left.IN1);
  digitalWrite(BL_BIN2, msg.motor_driver_back.motor_left.IN2);
  // digitalWrite(BL_PWM, msg.motor_driver_front.motor_right.pwm);
  ledcWrite(ledChannel4, msg.motor_driver_back.motor_left.pwm);
  
  
  
  

}

ros::Subscriber<pnf_agv::Holo_agv> agv_sub("agv_controller", &motorCb );

void setup() {

  nh.initNode();

  nh.subscribe(agv_sub);

  ledcSetup(ledChannel1, freq, resolution);
  ledcSetup(ledChannel2, freq, resolution);
  ledcSetup(ledChannel3, freq, resolution);
  ledcSetup(ledChannel4, freq, resolution);
  ledcAttachPin(FR_PWM,      ledChannel1);
  ledcAttachPin(FL_PWM,      ledChannel2);
  ledcAttachPin(BR_PWM,      ledChannel3);
  ledcAttachPin(BL_PWM,      ledChannel4);
  
  //Serial.begin (57600);

  pinMode(MD1_STBY, OUTPUT);
  pinMode(MD2_STBY, OUTPUT);
  pinMode(FR_AIN1, OUTPUT);
  pinMode(FR_AIN2, OUTPUT);
  pinMode(FL_BIN1, OUTPUT);
  pinMode(FL_BIN2, OUTPUT);
  pinMode(BR_AIN1, OUTPUT);
  pinMode(BR_AIN2, OUTPUT);
  pinMode(BL_BIN1, OUTPUT);
  pinMode(BL_BIN2, OUTPUT);

  // pinMode(FR_PWM, OUTPUT);
  // pinMode(FL_PWM, OUTPUT);
  // pinMode(BR_PWM, OUTPUT);
  // pinMode(BL_PWM, OUTPUT);
  
  digitalWrite(MD1_STBY, HIGH);
  digitalWrite(MD2_STBY, HIGH);
  



}

void loop(){
  nh.spinOnce();
}
