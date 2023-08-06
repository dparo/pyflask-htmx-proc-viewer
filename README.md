# pyflask-htmx-proc-viewer

An HTML based list of linux running processes using [Flask](https://flask.palletsprojects.com/en/2.3.x/) and [htmx](https://htmx.org/).

Allows to:
  - Run new bash commands
  - See a list of running processes
  - Terminate running processes with different signals (`SIGTERM`, `SIGINT`, `SIGKILL`).


## How it works
The HTML is rendered in the server (SSR) thanks to Flask. 
Web page reactivity is achieved trough the usage of htmx.

Htmx allows to hotswap snippets of HTML by invoking HTTP endpoints when specific events occur.
Allowing the frontend application to be almost JS (except the HTMX runtime itself) and JSON free.
By using Server Side Rendering (SSR), the latency required for first paint is reduced.

The responsability of validation and styling, is however, is completely shifted to the server.


## Preview

![image](https://github.com/dparo/pyflask-htmx-proc-viewer/assets/30259883/12a366e4-7401-4796-845c-038107857c67)


## Requirements

```bash
pip3 install flask
```

## Running

```bash
flask run --debug
```

Navigate to `http://127.0.0.1:5000/`
