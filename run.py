from runners.steps import retrieve_steps
from runners.heart_rate import retrieve_heart_rate
from runners.sleep import retrieve_sleep
from runners.body_battery import retrieve_body_battery
from runners.calories import retrieve_calories
from runners.stress import retrieve_stress

if __name__ == '__main__':
    retrieve_steps()
    retrieve_heart_rate()
    retrieve_sleep()
    retrieve_body_battery()
    retrieve_calories()
    retrieve_stress()
