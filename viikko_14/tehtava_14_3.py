"""
Tehtävä 14.3
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

from datetime import datetime, timedelta

def main():

    def ten_days_from_now():
        """Palauttaa datetime objektin 10 päivää eteenpäin tämänhetkisestä päivämäärästä."""
        return datetime.today() + timedelta(days=10)

    t_p = ten_days_from_now()

    print("Päivämäärä %d päivää tästä päivästä on: %s" % (10, t_p.strftime("%d.%m.%Y")))


if __name__ == "__main__":
    main()