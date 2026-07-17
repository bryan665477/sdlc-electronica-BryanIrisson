from hola_sensor import Sensor

def test_sensor_read_returns_correct_value():
    mi_sensor = Sensor()
    assert mi_sensor.read() == 23.5