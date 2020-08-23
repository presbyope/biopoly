import numpy as np

# return chirp rate in chirps per minute
def chirprate(temperature=25, pressure=760, humidity=15, wind_speed=2, number_crickets=5):
    # formula parameters for chirp rate
    T0 = 40/9
    m = 54/7
    
    # identify the independent variable
    ind = 0
    if type(temperature) is np.ndarray:
        ind = temperature
    elif type(pressure) is np.ndarray:
        ind = pressure
    elif type(humidity) is np.ndarray:
        ind = humidity
    elif type(wind_speed) is np.ndarray:
        ind = wind_speed
    elif type(number_crickets) is np.ndarray:
        ind = number_crickets
    
    # generate some noise in the independent variable
    noise_amplitude = 1.0
    noise = np.random.normal(size=len(ind)) * noise_amplitude + number_crickets/1000 + humidity/100 - wind_speed/25 + pressure/10000

    # perform final calculation
    return (temperature - T0 + noise) * m
    
# return time to next chrip in seconds
def chirptime(T):
    return 60/chirprate(T)