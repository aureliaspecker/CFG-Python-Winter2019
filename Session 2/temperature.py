def fahrenheit(temperature_in_celsius):
    """ Returns the temperature in degrees Fahrenheit """
    return (temperature_in_celsius * 9.0 / 5.0) + 32

for t in (22, 0, -10, 13):
    print "{} : {}".format(t, fahrenheit(t))