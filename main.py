import js
import asyncio
from pyodide.ffi import create_proxy, to_js

e = js.React.createElement

def a(*args): return js.Array(*args)
def o(**kwargs): return js.Object.fromEntries(to_js(kwargs))

checkbox_src="data:image/svg+xml;base64,PHN2ZwogICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICAgdmlld0JveD0iMCAwIDI0IDI0IgogICAgZmlsbD0ibm9uZSIKICAgIHN0cm9rZT0iI2ZmZiIKICAgIHN0cm9rZS13aWR0aD0iNCIKICAgIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIKICAgIHN0cm9rZS1saW5lam9pbj0icm91bmQiCj4KPHBvbHlsaW5lIHBvaW50cz0iMjAgNiA5IDE3IDQgMTIiPjwvcG9seWxpbmU+Cjwvc3ZnPgoK"

def LabeledCheckbox(props={}, children=[], *args, **kwargs):
    return e('div', o(className="checkbox-with-label"),
        e('div', o(className="checkbox-container"),
            e('input', o(type="checkbox", checked=props.checked, onChange=props.onChange, id=props.id), None),
            e('img', o(className="checkmark", src=checkbox_src), None),
        ),
        e('label', o(htmlFor=props.id), props.label),
    )

@create_proxy
def App(props={}, children=[], *args, **kwargs):
    count, set_count = js.React.useState(0)
    use_delay, set_use_delay = js.React.useState(False)

    # useEffect and asyncio
    @create_proxy
    def onLoad():
        @create_proxy
        async def onLoadInner():
            await asyncio.sleep(1)
            set_use_delay(True)
        onLoadInner()

    # js.React.useEffect(onLoad, a()) # Uncomment to test useEffect

    # Nested functions and async
    @create_proxy
    def handle_inc(i):
        @create_proxy
        async def handle_click(event):
            if use_delay:
                await asyncio.sleep(1.5)
            set_count(create_proxy(lambda count: count + i))
        return handle_click

    # Standard setState
    def toggleDelay(e):
        set_use_delay(e.target.checked)

    return e('div', None,
        e('p', o(className="count"), count),
        e('div', o(className="buttons"),
            e('button', o(onClick=handle_inc(1)), '+'),
            e('button', o(onClick=handle_inc(-1)), '-'),
        ),
        LabeledCheckbox(o(checked=use_delay, onChange=toggleDelay, id="use_delay", label="Use delay")),
    )

App
