import { useState } from "react"
import api from "../api/api"

function Login() {

    const [usuario, setUsuario] = useState("")
    const [password, setPassword] = useState("")

    const handleLogin = async (e) => {

        e.preventDefault()

        try {

            const response = await api.post(
                "/auth/login",
                {
                    usuario,
                    password
                }
            )

            console.log(response.data)

            localStorage.setItem(
                "token",
                response.data.access_token
            )

            alert("Login correcto")

        } catch (error) {

            console.error(error)

            alert("Usuario o contraseña incorrectos")
        }
    }

    return (

        <div className="min-h-screen bg-gray-100 flex items-center justify-center">

            <form
                onSubmit={handleLogin}
                className="bg-white p-8 rounded-2xl shadow-lg w-full max-w-md"
            >

                <h1 className="text-3xl font-bold mb-6 text-center text-blue-600">
                    SysVen
                </h1>

                <input
                    type="text"
                    placeholder="Usuario"
                    value={usuario}
                    onChange={(e) => setUsuario(e.target.value)}
                    className="w-full border p-3 rounded-lg mb-4"
                />

                <input
                    type="password"
                    placeholder="Contraseña"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full border p-3 rounded-lg mb-4"
                />

                <button
                    type="submit"
                    className="w-full bg-blue-600 text-white p-3 rounded-lg hover:bg-blue-700"
                >
                    Ingresar
                </button>

            </form>

        </div>
    )
}

export default Login