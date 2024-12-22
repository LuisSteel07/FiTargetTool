import io
import json

from Model.Ejercicios import Ejercicios

new_ejer = Ejercicios("gato", [12,12,12,12], [12,23,234,23])

p = io.open("test_json.json", 'r')
data: dict = json.loads(p.read())
p.close()

dict_ejers = {
    "name": new_ejer.name[0],
    "reps": new_ejer.reps[0],
    "weights": new_ejer.weights
}

data['ejers'].append(json.dumps(dict_ejers))

p = io.open("test_json.json", "w+")
p.write(json.JSONEncoder().encode(data))
p.close()