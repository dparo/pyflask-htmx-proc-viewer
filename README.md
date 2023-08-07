# pyflask-htmx-proc-viewer

An HTML based list of linux running processes using [Flask](https://flask.palletsprojects.com/en/2.3.x/) and [htmx](https://htmx.org/).

Allows to:
  - Run new bash commands
  - See a list of running processes
  - Terminate running processes with different signals (`SIGTERM`, `SIGINT`, `SIGKILL`).


## How it works
The HTML is rendered in the server (SSR) thanks to Flask. 
Web page reactivity is achieved trough the usage of htmx.

Htmx allows to hotswap fragments of HTML by invoking HTTP endpoints when specific client events occur (user clicks on a button).
This paradigm allows the webapp to be free of JSON and JS (except the HTMX runtime itself).
By using Server Side Rendering (SSR), the latency required for Largest Contentful Paint (LCF) is reduced.

The responsability of validation and styling, however, is completely shifted to the server.

See this [Vue Docs paragraph](https://vuejs.org/guide/scaling-up/ssr.html#why-ssr) for the benefits of SSR.

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
