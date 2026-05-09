import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom"

import DashboardLayout from "./layouts/DashboardLayout"

import Dashboard from "./pages/Dashboard"
import Productos from "./pages/Productos"
import Categorias from "./pages/Categorias"
import Ventas from "./pages/Ventas"
import Usuarios from "./pages/Usuarios"
import Reportes from "./pages/Reportes"


function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<DashboardLayout />}>

          <Route index element={<Dashboard />} />

          <Route
            path="productos"
            element={<Productos />}
          />

          <Route
            path="categorias"
            element={<Categorias />}
          />

          <Route
            path="ventas"
            element={<Ventas />}
          />

          <Route
            path="usuarios"
            element={<Usuarios />}
          />

          <Route
            path="reportes"
            element={<Reportes />}
          />

        </Route>

      </Routes>

    </BrowserRouter>
  )
}

export default App