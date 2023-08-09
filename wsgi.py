import os
import signal
import subprocess
from dataclasses import dataclass
import shlex

from flask import (Flask, make_response, render_template,
                   render_template_string, request, send_from_directory, Markup, redirect)

app = Flask(__name__)


@dataclass
class Proc:
    pid: int
    argv: str


@app.delete("/api/pid/<int:id>")
def kill_pid(id: int):
    sigstr = request.args["signal"] or "SIGINT"
    print(f"Killing {id} with signal = {sigstr}")
    os.kill(id, signal.Signals[sigstr].value)
    response = make_response("")
    response.headers["HX-Trigger"] = "evProcListRefresh"
    return response


@app.post("/api/cmd")
def new_cmd():
    new_proc = subprocess.Popen(request.form["cmd"], shell=True)
    new_pid = new_proc.pid
    response = make_response(Markup.escape(f'Created new process with pid {new_pid}'))
    response.headers["HX-Trigger"] = "evProcListRefresh"
    return response


@app.route("/api/procs")
def get_procs():
    pids = list(filter(lambda x: x.isnumeric(), list(os.listdir("/proc"))))
    pids = sorted([int(x) for x in pids])

    cmds = []
    for p in pids:
        try:
            with open(f"/proc/{p}/cmdline", "r") as f:
                argv = f.read()
                argv = argv.replace("\u0000", " ").strip()

                # Skip Zombie (Z), Dead (X), Stopped (T) processes
                with open(f"/proc/{p}/stat", "r") as f:
                    stat = f.read().split()
                    state_idx = 1
                    while not stat[state_idx].endswith(')'):
                        state_idx += 1
                    state = stat[state_idx + 1]
                    if state in ['R', 'S', 'I']: # Running, Sleeping, Idle
                        cmds.append(Proc(p, argv))

        except Exception:
            pass

    # Bump the factor to simulate a huge list
    cmds = cmds * 1
    return {
        "cnt": len(cmds),
        "cmds": cmds,
    }


@app.get("/procs")
def html_procs():
    procs = get_procs()
    return render_template('proc_list.xhtml', cmds=procs['cmds'])


@app.route("/")
def index_route():
    procs = get_procs()
    refresh_time_msecs = 10000 * 1000
    return render_template(
        "index.xhtml", refresh_time_msecs=refresh_time_msecs,
        cmds=procs['cmds']
    )

@app.route("/index")
@app.route("/index.html")
def index_redirect():
    return redirect("/")
