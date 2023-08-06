import os
import signal
import subprocess
from dataclasses import dataclass

from flask import (Flask, make_response, render_template,
                   render_template_string, request, send_from_directory)

app = Flask(__name__)


@dataclass
class Proc:
    pid: int
    argv: str


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


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
    subprocess.Popen(request.form["cmd"], shell=True)
    response = make_response("")
    response.headers["HX-Trigger"] = "evProcListRefresh"
    return response


@app.route("/api/procs")
def get_procs():
    pids = list(filter(lambda x: x.isnumeric(), list(os.listdir("/proc"))))
    pids = [int(x) for x in pids]

    cmds = []
    for p in pids:
        try:
            with open(f"/proc/{p}/cmdline", "r") as f:
                argv = f.read()
                argv = argv.replace("\u0000", " ").strip()
                cmds.append(Proc(p, argv))
        except Exception:
            pass

    return {
        "cnt": len(pids),
        "cmds": cmds,
    }


@app.get("/procs")
def html_procs():
    procs = get_procs()
    return render_template_string(
        """
        <ul class="list-disc" hx-get="/procs" hx-trigger="evProcListRefresh from:body" hx-swap="outerHTML">
            {% for cmd in cmds %}
                <li id="li-{{ cmd.pid }}">
                    {% for signal in ['SIGTERM', 'SIGINT', 'SIGKILL'] %}
                    <button hx-delete="/api/pid/{{ cmd.pid }}?signal={{ signal }}" hx-swap="outerHTML" hx-target="closest li"
                        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">{{ signal }}</button>
                    {% endfor %}
                    {{ cmd.pid }} - {{ cmd.argv }}

                </li>
            {% endfor %}
        </ul>
        """,
        cmds=procs["cmds"],
    )


@app.route("/")
def index_route():
    proc_list = html_procs()
    refresh_time_msecs = 10000 * 1000
    return render_template(
        "index.xhtml", html_proc_list=proc_list, refresh_time_msecs=refresh_time_msecs
    )
