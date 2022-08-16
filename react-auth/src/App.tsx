import "./App.css";
import { Login } from "./components/Login";
import { Register } from "./components/Register";
import { Nav } from "./components/Nav";
import { Home } from "./components/Home";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
    return (
        <BrowserRouter>
            <Nav />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
