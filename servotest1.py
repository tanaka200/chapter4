import time
import RPi.GPIO as GPIO

# 初期化処理
def initialize_servo():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    servo = GPIO.PWM(2, 50)
    servo.start(0.0)
    return servo

# 角度からデューティーサイクルを計算
def calculate_duty_cycle(angle):
    # 角度からデューティーサイクルを計算します
    if angle < -90:
        angle = -90
    elif angle > 90:
        angle = 90
    return 7.25 + (angle / 90) * 4.75

# サーボモータを指定した角度に移動する関数
def setservo(servo, angle):
    duty_cycle = calculate_duty_cycle(angle)
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(1.0)

# メインプログラム
if __name__ == "__main__":
    servo = initialize_servo()
    
    try:
        for i in range(5):
            setservo(servo, -90)  # -90度
            time.sleep(1.0)

            setservo(servo, 0)    # 0度
            time.sleep(1.0)

            setservo(servo, 90)   # 90度
            time.sleep(1.0)
    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
