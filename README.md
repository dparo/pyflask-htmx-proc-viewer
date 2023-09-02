# pyflask-htmx-proc-viewer

An HTML based list of linux running processes using [Flask](https://flask.palletsprojects.com/en/2.3.x/) and [HTMX](https://htmx.org/).

Allows to:

- Run new bash commands
- See a list of running processes
- Terminate running processes with different signals (`SIGTERM`, `SIGINT`, `SIGKILL`).

## How it works

The HTML is rendered in the server (SSR) thanks to Flask.
Web page reactivity is achieved through the usage of htmx.

HTMX is a declarative client side JS-runtime which enables the server to directly influence the DOM through partial updates.
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

### Disadvantages

- HTMX requires always a server up-and-running to serve the HTML fragments.
  Such solution may not be ideal for client-side heavy applications (eg: a painting/drawing application saving locally),
  A JS framework/bundle in these cases may be more appropriate, including for applications target at WebUI sandbox/distributions -- for example: [Electron](https://www.electronjs.org/), [NwJS](https://nwjs.io/).

- HTMX to be scalable requires a strong HTML templating engine, or equivalently a programming language with DSL capabilities, to create reusable, parametrizable snippets of HTML (aka Components).
  Note that, in React land, this is achieved thanks to JSX.
  Python+(Flask/FastAPI/Django) provides a powerful templating engine [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) with support for even [templating inheritance](https://jinja.palletsprojects.com/en/3.1.x/templates/#template-inheritance).
  Java+[Spring](https://spring.io/) can lavarage the [Thymeleaf](https://www.thymeleaf.org/) templating engine.
  Golang also provides in its standard a simpler and more pragmatic [html templating engine](https://pkg.go.dev/html/template).
  Rust can leverage DSL capabilities thanks to the usage of [macros](https://doc.rust-lang.org/book/ch19-06-macros.html), to provide a more JSX-like syntax. See for example [leptos::view!() macro](https://docs.rs/leptos/latest/leptos/macro.view.html)

#### Solution

[Alpine.js](https://alpinejs.dev/), an HTML-focused client side model framework, pairs nicely with [HTMX](https://htmx.org/).
Alpine.js can aid in implementing state-management and interactivity for operations that are purely client side (eg: dropdowns, spinners, searchboxes etc),
where waiting a full RTT to the server to update the DOM would be costly or unnecessary.

## Server Side Routing

Navigating the website is achieved through server side routing. This means that a visit to a new URL link issues a full HTML page refresh, causing possible flashiness and flickering.
SPAs do not suffer from this problem.
In SSR, This can be fixed by using the modern [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API) exposed from browsers,
to animate/fade elements when transitioning from a page to another.

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
