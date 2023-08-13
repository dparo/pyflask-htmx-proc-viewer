# pyflask-htmx-proc-viewer

An HTML based list of linux running processes using [Flask](https://flask.palletsprojects.com/en/2.3.x/) and [HTMX](https://htmx.org/).

Allows to:
  - Run new bash commands
  - See a list of running processes
  - Terminate running processes with different signals (`SIGTERM`, `SIGINT`, `SIGKILL`).


## How it works
The HTML is rendered in the server (SSR) thanks to Flask.
Web page reactivity is achieved through the usage of htmx.

HTMX is a declaritive client side JS-runtime which enables the server to directly influence the DOM through partial updates.
Partial updates are achieved by hotswapping fragments of HTML generated from the server,
when specific client side events occurs (eg: user clicks on a button).
HTMX places the returned HTML fragment in the DOM by following some rules specified within the HTML itself.
This is in contrast to traditional SPA frameworks (like React or Angular), where REST endpoints typically returns
JSON objects (subject to schema constraints) which are then deserialized and used to update the DOM
from within the JS browser runtime itself.
HTMX, like any other Server Side Rendering (SSR) focused technology,
allows to reduce the round trip time and processing at the client side to update the view.
It also provides a simpler alternative and breath of fresh air, from a software landscape dominated by convoluted (JS/NPM)-heavy frameworks.

See this [Vue Docs paragraph](https://vuejs.org/guide/scaling-up/ssr.html#why-ssr) for the benefits of SSR.

### Future work
[Alpine.js](https://alpinejs.dev/), an HTML-focused client side model framework, pairs nicely with [HTMX](https://htmx.org/).
Alpine.js can aid in implementing state-management and interactivity for operations that are purely client side (eg: dropdowns, spinners, etc).


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
