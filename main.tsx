import * as React from "react"
import { createRoot } from "react-dom/client"
import { loadPyodide } from "pyodide"

import App_src from "./main.py"

window.React = React // Bind to js.React within Pyodide

async function main() {
    console.log("Loading Pyodide...")
    let pyodide = await loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.28.2/full/"
    });
    pyodide.setDebug(true)
    console.log("Loaded Pyodide")

    const App = pyodide.runPython(App_src)

    const root = document.getElementById("app")
    root!.classList.remove("loading")
    createRoot(root!).render(<App />)
}

main();

