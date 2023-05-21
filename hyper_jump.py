import datetime
import bcrypt, time, random

def r2d2_sleep():
    time.sleep(random.randint(0,100)*0.006)
    for i in range(0, random.randint(1,4)):
        bcrypt.hashpw('A'.encode()*99999, bcrypt.gensalt())
    return None

def launch_timer():
    launch_warning_time = int(time.time())
    print('Warning !!!\n')
    r2d2_sleep()
    print('Starting the countdown:\n')
    for i in range(5,0,-1):
        r2d2_sleep()
        print(i)
    r2d2_sleep()
    print('\nStarting engines')

    engine_run_time = int(time.time())

    for i in range(0,2):
        print("🔥<*", end="")
        r2d2_sleep()
    for i in range(0,2):
        print("<*<*<*", end="")
        r2d2_sleep()
    for i in range(0,2):
        print("<*<*<*<*<*<*<*<*", end="")
        r2d2_sleep()
    print()
    print('Tsshhhhhhhhhhhh.......')
    for i in range(0,10):
        print('.', end=".")
        time.sleep(0.1)
    for i in range(0,11):
        print('.', end=".")
        time.sleep(0.1)
    for i in range(0,12):
        print('.', end=".")
        time.sleep(0.1)
    for i in range(0,13):
        print('.', end=".")
        time.sleep(0.1)
    print('\n')
    return launch_warning_time, engine_run_time

def x_wing_flight(launch_warning_time, engine_run_time, flag):
    seed = random.randint(launch_warning_time, engine_run_time)
    random.seed(seed)
    coordinates_encrypted = []
    for c in flag:
        magic_int = random.randint(1,100)
        coordinates_encrypted.append(ord(c)*magic_int)

    return coordinates_encrypted


flag = "OmWars{test_flag}"

lt, et = launch_timer()
coordinates_encrypted = x_wing_flight(lt, et, flag)

print(coordinates_encrypted)
print(datetime.date.today())

#[4503, 1199, 3132, 388, 912, 805, 10824, 3528, 3560, 2000, 260, 3690, 1995, 3478, 7956, 8829, 5680, 3621, 5472, 4655, 108, 5712, 384, 618, 260, 4560, 264, 1440, 9996, 7035, 10670, 3399, 1250]
#2023-01-17