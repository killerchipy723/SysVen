import {
    FaBox,
    FaCashRegister,
    FaChartBar,
    FaHome,
    FaTags,
    FaUsers
} from "react-icons/fa"

import {
    Outlet,
    Link
} from "react-router-dom"


function DashboardLayout() {

    return (

        <div className="flex min-h-screen bg-gray-100">

            {/* SIDEBAR */}

            <aside className="w-64 bg-gray-900 text-white flex flex-col">

                {/* LOGO */}

                <div className="p-6 text-2xl font-bold border-b border-gray-700">

                    SysVen 1.0

                </div>

                {/* MENU */}

                <nav className="flex-1 p-4">

                    <ul className="space-y-2">

                        {/* INICIO */}

                        <li>

                            <Link
                                to="/"
                                className="w-full flex items-center gap-3 p-3 rounded-lg hover:bg-gray-800 transition"
                            >

                                <FaHome />

                                Inicio

                            </Link>

                        </li>

                        {/* PRODUCTOS */}

                        <li>

                            <Link
                                to="/productos"
                                className="w-full flex items-center gap-3 p-3 rounded-lg hover:bg-gray-800 transition"
                            >

                                <FaBox />

                                Productos

                            </Link>

                        </li>

                        {/* CATEGORIAS */}

                        <li>

                            <Link
                                to="/categorias"
                                className="w-full flex items-center gap-3 p-3 rounded-lg hover:bg-gray-800 transition"
                            >

                                <FaTags />

                                Categorías

                            </Link>

                        </li>

                        {/* VENTAS */}

                        <li>

                            <Link
                                to="/ventas"
                                className="w-full flex items-center gap-3 p-3 rounded-lg hover:bg-gray-800 transition"
                            >

                                <FaCashRegister />

                                Ventas

                            </Link>

                        </li>

                        {/* REPORTES */}

                        <li>

                            <Link
                                to="/reportes"
                                className="w-full flex items-center gap-3 p-3 rounded-lg hover:bg-gray-800 transition"
                            >

                                <FaChartBar />

                                Reportes

                            </Link>

                        </li>

                        {/* USUARIOS */}

                        <li>

                            <Link
                                to="/usuarios"
                                className="w-full flex items-center gap-3 p-3 rounded-lg hover:bg-gray-800 transition"
                            >

                                <FaUsers />

                                Usuarios

                            </Link>

                        </li>

                    </ul>

                </nav>

            </aside>

            {/* CONTENIDO */}

            <main className="flex-1 flex flex-col">

                {/* TOPBAR */}

                <header className="bg-white shadow px-6 py-4 flex justify-between items-center">

                    <h1 className="text-2xl font-bold text-gray-700">

                        Sistema de Gestión Comercial

                    </h1>

                    <div className="font-semibold text-gray-600">

                        Administrador

                    </div>

                </header>

                {/* CONTENIDO DINÁMICO */}

                <div className="p-6 flex-1">

                    <Outlet />

                </div>

            </main>

        </div>
    )
}

export default DashboardLayout