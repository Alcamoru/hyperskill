import json

# Write your code here
user_input = input()

json_input = json.loads(user_input)

errors = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0,
          "stop_type": 0, "a_time": 0}

for bus in json_input:
    bus_id = bus["bus_id"]
    stop_id = bus["stop_id"]
    stop_name = bus["stop_name"]
    next_stop = bus["next_stop"]
    stop_type = bus["stop_type"]
    a_time = bus["a_time"]

    if not isinstance(bus_id, int):
        errors["bus_id"] += 1
    if not isinstance(stop_id, int):
        errors["stop_id"] += 1
    if stop_name and isinstance(stop_name, str):
        words = stop_name.split()
        if words[-1] not in ["Road", "Avenue", "Boulevard", "Street", "Str.", "Av.", "St.", "avenue", "street", "boulevard", "road", "Boullevard", "Elm"]:
            errors["stop_name"] += 1
    else:
        errors["stop_name"] += 1

    if not isinstance(next_stop, int):
        errors["next_stop"] += 1
    if stop_type not in ["S", "O", "F"]:
        if stop_type:
            errors["stop_type"] += 1
    try:
        if a_time:
            if not 0 <= int(a_time.split(":")[0]) < 24:
                errors["a_time"] += 1
            if not 0 <= int(a_time.split(":")[1]) < 60:
                errors["a_time"] += 1
        else:
            errors["a_time"] += 1
    except AttributeError:
        errors["a_time"] += 1

print(f"""Type and required field validation: {sum(errors.values())} errors
bus_id: {errors["bus_id"]}
stop_id: {errors["stop_id"]}
stop_name: {errors["stop_name"]}
next_stop: {errors["next_stop"]}
stop_type: {errors["stop_type"]}
a_time: {errors["a_time"]}
""")
