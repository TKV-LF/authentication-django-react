import { useEffect, useState } from "react";
import axios from "axios";

export const Home = () => {
    const [message, setMessage] = useState("You are not authenticated");
    useEffect(() => {
        (async () => {
            try {
                axios.defaults.withCredentials = true;
                const response = await axios.get("http://localhost:8000/api/user");

                const user = response.data;

                setMessage(`Hi ${user.first_name} ${user.last_name}`);
            } catch (e) {
                setMessage("You are not authenticated");
            }
        })();
    }, []);
    return (
        <div className="container mt-5 text-center">
            <h3>{message}</h3>
        </div>
    );
};
