import pickle
import ast
import time
import os
class DataModule:
    def load(self, file, key, default=None):
        try:
            f = open(file)
        except FileNotFoundError:
            f = open(file, "w")
        for lin in f:
            lin = lin.strip()
            counter = 0
            dkey = ""
            InData = ""
            tup = ""  # Initialize tup to an empty string

            for s in lin:
                if s == "$":
                    counter += 1
                elif counter == 0:
                    dkey += s
                elif counter == 1:
                    if dkey != key:
                        continue
                    tup = s  # Assign a value to tup
                else:
                    InData += s
            if dkey == key:  # Check if the key matches
                if tup == "n":
                    return None
                elif tup == "s":
                    return str(InData)
                elif tup == "i":
                    return int(InData)
                elif tup == "f":
                    return float(InData)
                elif tup == "l":
                    return ast.literal_eval(InData)
                elif tup == "d":
                    # Remove the curly braces and parse the dictionary data
                    InData = InData.strip("{}")
                    data_dict = {}
                    pairs = InData.split(", ")
                    for pair in pairs:
                        key_value = pair.split(": ")
                        data_dict[key_value[0].strip("'")] = int(key_value[1])
                    return data_dict
                else:
                    return InData
        return default  # Return  if the key is not found

    def save(self,file, key, data):
        if isinstance(data, str):
            typ = "s"
        elif isinstance(data, int):
            typ = "i"
        elif isinstance(data, float):
            typ = "f"
        elif isinstance(data, list):
            typ = "l"
        elif isinstance(data, dict):
            typ = "d"
        elif data == None:
            typ = "n"

        line = f"{key}${typ}${data}\n"
        if not os.path.exists(file):
            # Create the file if it does not exist
            open(file, 'w').close()
        # Check if the key already exists in the file
        with open(file, "r+") as f:
            lines = f.readlines()
            for i, lin in enumerate(lines):
                lin = lin.strip()
                if lin.startswith(key + "$"):
                    # Replace the existing line
                    lines[i] = line
                    break
            else:
                # Add a new line if the key doesn't exist
                lines.append(line)

            # Move the file pointer to the beginning of the file
            f.seek(0)
            # Write the updated lines to the file
            f.writelines(lines)
            # Truncate the file to remove any remaining old content
            f.truncate()