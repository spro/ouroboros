import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import Inspect from "vite-plugin-inspect"

function PythonReader() {
    return {
        name: "python-reader",
        transform(src: string, id: string) {
            if (id.endsWith(".py")) {
                console.log("src", src)
                return {
                    // code: `console.log(${src})`,
                    code: `const py_src = ${JSON.stringify(src)}\nexport default py_src`,
                    map: null,
                }
            }
        }
    }
}

// https://vite.dev/config/
export default defineConfig({
    plugins: [react(), Inspect(), PythonReader()],
})
