
from flask import Flask
import platform

app = Flask(__name__)

@app.route("/system_info")
def system_info():
    system_info = {
        "Operating System": platform.system(),
        "Machine":  platform.machine(),
        "Processor":  platform.processor()
    }
    return str(system_info)

app.run(debug=True)