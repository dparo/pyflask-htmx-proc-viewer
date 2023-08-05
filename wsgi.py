from flask import Flask, render_template, render_template_string
import os
from dataclasses import dataclass
from markupsafe import escape
import signal
from flask import request

app = Flask(__name__)

@dataclass
class Proc:
    pid: int
    argv: str


@app.route("/api/pid/<int:id>", methods=['DELETE'])
def kill_pid(id: int):
    os.kill(id, signal.SIGINT)
    return ""

@app.route("/api/procs")
def get_procs():
    pids = list(filter(lambda x: x.isnumeric(), list(os.listdir('/proc'))))
    pids = [int(x) for x in pids]

    cmds = []
    for p in pids:
        try:
            with open(f'/proc/{p}/cmdline', 'r') as f:
                argv = f.read()
                argv = argv.replace('\u0000', ' ').strip()
                cmds.append(Proc(p, argv))
        except Exception:
            pass

    return {
        "cnt": len(pids),
        "cmds": cmds,
    }

@app.route("/")
def index_route():
    procs = get_procs()
    refresh_time_msecs = 10000 * 1000
    return render_template('index.xhtml',
                           cmds=procs['cmds'],
                           refresh_time_msecs=refresh_time_msecs)
