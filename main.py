from pymavlink import mavutil
import logging
from pynput import keyboard
import threading
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)


class Vehicle:
    def __init__(self):
        self.the_connection = mavutil.mavlink_connection('udp:localhost:14550')
        logging.info("Waiting heartbeat...")
        self.the_connection.wait_heartbeat()
        logging.info("Received heartbeat!")
        logging.info("Heartbeat from system (system %u component %u)" % (
            self.the_connection.target_system, self.the_connection.target_component))
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.yaw_rate = 0
        self.running = True

    def receive_heartbeat_messages(self):
        with open("heartbeat_log.txt", "a") as file:
            while self.running:
                msg = self.the_connection.recv_match(type="HEARTBEAT", blocking=True)
                if msg:
                    msg_dict = msg.to_dict()
                    file.write(str(msg_dict) + "\n")
                    file.flush()

    def arm(self):
        self.the_connection.mav.command_long_send(
            self.the_connection.target_system, self.the_connection.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
        msg = self.the_connection.recv_match(type="COMMAND_ACK", blocking=True)  # 0 => Accepted
        logging.info(msg)
        if msg is None:
            logging.warning("No COMMAND_ACK received")
        elif msg.command == mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM:
            if msg.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
                logging.info("Vehicle armed!")
            else:
                logging.info(f"Vehicle couldn't arm, result={msg.result}")
        else:
            logging.info(f"Ignored COMMAND_ACK for command {msg.command}")

    def disarm(self):
        self.the_connection.mav.command_long_send(
            self.the_connection.target_system, self.the_connection.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 0, 0, 0, 0, 0, 0, 0)
        msg = self.the_connection.recv_match(type="COMMAND_ACK", blocking=True)  # 0 => Accepted
        logging.info(msg)
        if msg is None:
            logging.warning("No COMMAND_ACK received")
        elif msg.command == mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM:
            if msg.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
                logging.info("Vehicle disarmed!")
            else:
                logging.info(f"Vehicle couldn't disarm, result={msg.result}")
        else:
            logging.info(f"Ignored COMMAND_ACK for command {msg.command}")

    def send_movement(self):
        self.the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(
            0,
            self.the_connection.target_system,
            self.the_connection.target_component,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            int(0b0000111111000111),
            0, 0, 0,
            self.vx, self.vy, self.vz,
            0, 0, 0,
            0, self.yaw_rate
        ))
        logging.info(f"x={self.vx} y={self.vy} z={self.vz} yaw={self.yaw_rate}")

    def on_press(self, key):
        try:
            if key.char == 'w':
                self.vx = 1
            elif key.char == 's':
                self.vx = -1
            elif key.char == 'a':
                self.vy = -1
            elif key.char == 'd':
                self.vy = 1
            elif key.char == 'q':
                self.arm()
            elif key.char == 'e':
                self.disarm()
        except AttributeError:
            if key == keyboard.Key.up:
                self.vz = -1
            elif key == keyboard.Key.down:
                self.vz = 1
            elif key == keyboard.Key.left:
                self.yaw_rate = -0.5
            elif key == keyboard.Key.right:
                self.yaw_rate = +0.5
            elif key == keyboard.Key.esc:
                self.running = False
                return False

    def movement_loop(self):
        while self.running:
            self.send_movement()
            time.sleep(0.05)

    def on_release(self, key):
        try:
            if key.char in ('w', 's'):
                self.vx = 0
            elif key.char in ('a', 'd'):
                self.vy = 0
        except AttributeError:
            if key in (keyboard.Key.up, keyboard.Key.down):
                self.vz = 0
            elif key in (keyboard.Key.left, keyboard.Key.right):
                self.yaw_rate = 0


v = Vehicle()
# v.receive_heartbeat_messages()
movement_thread = threading.Thread(
    target=v.movement_loop,
    daemon=True
)
movement_thread.start()

heartbeat_thread = threading.Thread(
    target=v.receive_heartbeat_messages,
    daemon=True
)
heartbeat_thread.start()

logging.info("Keyboard mode active")

with keyboard.Listener(
    on_press=v.on_press,
    on_release=v.on_release
) as listener:
    listener.join()

logging.info("The program has been closed!")
