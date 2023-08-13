# pyflask-htmx-proc-viewer

An HTML based list of linux running processes using [Flask](https://flask.palletsprojects.com/en/2.3.x/) and [htmx](https://htmx.org/).

Allows to:
  - Run new bash commands
  - See a list of running processes
  - Terminate running processes with different signals (`SIGTERM`, `SIGINT`, `SIGKILL`).


## How it works
The HTML is rendered in the server (SSR) thanks to Flask.
Web page reactivity is achieved through the usage of htmx.

Htmx enables the server to directly apply partial updates to the DOM.
Partial updates are achieved by hotswapping fragments of HTML generated from the server,
when specific client side events occurs (eg: user clicks on a button).
This is in contrast to traditional SPA frameworks (like React or Angular), where REST endpoints returns
JSON objects (subject to schema constraints) which are then deserialized and used to update the DOM
from within the JS browser runtime itself.
HTMX, like any other Server Side Rendering (SSR) focused technologies,
allows to reduce the round trip time and processing at the client side to update the view.

The responsibility of validation and styling, however, is shifted to the server.

See this [Vue Docs paragraph](https://vuejs.org/guide/scaling-up/ssr.html#why-ssr) for the benefits of SSR.

[Alpine.js](https://alpinejs.dev/), an HTML-focused client side model framework,
can aid in implementing interactivity for operations that are purely client side (eg: dropdowns, spinners, etc).


## Preview

![image](https://github.com/dparo/pyflask-htmx-proc-viewer/assets/30259883/a841d461-6586-4f2b-97b1-0edb86deb4c5)


## Requirements

```bash
pip3 install flask
```

## Running

```bash
flask run --debug
```

Navigate to `http://127.0.0.1:5000/`
