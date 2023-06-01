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

const int PWM1=2;
const int PWM2=17;
const int PWM3=22;
const int PWM4=25;

const int MD1_AIN1=0;
const int MD1_AIN2=4;
const int MD1_BIN1=18;
const int MD1_BIN2=5;

const int MD1_STBY=13;

const int MD2_AIN1=15;
const int MD2_AIN2=23;
const int MD2_BIN1=27;
const int MD2_BIN2=26;

const int MD2_STBY=21;




void motorCb(const pnf_agv::Holo_agv& msg){
//  digitalWrite(MD1_STBY, HIGH);
//  digitalWrite(MD2_STBY, msg.motor_driver_back.stby);

  digitalWrite(MD1_AIN1, msg.motor_driver_front.motor_right.IN1);
  digitalWrite(MD1_AIN2, msg.motor_driver_front.motor_right.IN2);
  ledcWrite(ledChannel1, msg.motor_driver_front.motor_right.pwm);
  
  digitalWrite(MD1_BIN1, msg.motor_driver_front.motor_left.IN1);
  digitalWrite(MD1_BIN2, msg.motor_driver_front.motor_left.IN2);
  ledcWrite(ledChannel2, msg.motor_driver_front.motor_left.pwm);
  
  digitalWrite(MD2_AIN1, msg.motor_driver_back.motor_right.IN1);
  digitalWrite(MD2_AIN2, msg.motor_driver_back.motor_right.IN2);
  ledcWrite(ledChannel3, msg.motor_driver_back.motor_right.pwm);
  
  digitalWrite(MD2_BIN1, msg.motor_driver_back.motor_left.IN1);
  digitalWrite(MD2_BIN2, msg.motor_driver_back.motor_left.IN2);
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

  //Serial.begin (57600);

  pinMode(MD1_STBY, OUTPUT);
  pinMode(MD2_STBY, OUTPUT);
  pinMode(MD1_AIN1, OUTPUT);
  pinMode(MD1_AIN2, OUTPUT);
  pinMode(MD1_BIN1, OUTPUT);
  pinMode(MD1_BIN2, OUTPUT);
  pinMode(MD2_AIN1, OUTPUT);
  pinMode(MD2_AIN2, OUTPUT);
  pinMode(MD2_BIN1, OUTPUT);
  pinMode(MD2_BIN2, OUTPUT);

  digitalWrite(MD1_STBY, HIGH);
  digitalWrite(MD2_STBY, HIGH);
  
  ledcAttachPin(PWM1,      ledChannel1);
  ledcAttachPin(PWM2,      ledChannel2);
  ledcAttachPin(PWM3,      ledChannel3);
  ledcAttachPin(PWM4,      ledChannel4);


}

void loop(){
  nh.spinOnce();
}
