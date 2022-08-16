import React, { SyntheticEvent, useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";

export const Register = () => {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirm, setPasswordConfirm] = useState("");
    const [redirect, setRedirect] = useState(false);

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        await axios.post("http://localhost:8000/api/register", {
            first_name: firstName,
            last_name: lastName,
            email,
            password,
            password_confirm: passwordConfirm,
        });

        setRedirect(true);
    };

    if (redirect) {
        return <Navigate to="/login" />;
    }

    return (
        <main className="form-signin w-100 m-auto">
            <form onSubmit={submit}>
                <div className="form-floating">
                    <input
                        type="text"
                        className="form-control"
                        id="firstName"
                        placeholder="First Name"
                        onChange={(e) => setFirstName(e.target.value)}
                    />
                    <label htmlFor="floatingInput">First Name</label>
                </div>
                <div className="form-floating">
                    <input
                        type="text"
                        className="form-control"
                        id="lastName"
                        placeholder="Last Name"
                        onChange={(e) => setLastName(e.target.value)}
                    />
                    <label htmlFor="floatingInput">Last Name</label>
                </div>
                <div className="form-floating">
                    <input
                        type="email"
                        className="form-control"
                        id="email"
                        placeholder="name@example.com"
                        onChange={(e) => setEmail(e.target.value)}
                    />
                    <label htmlFor="email">Email address</label>
                </div>
                <div className="form-floating">
                    <input
                        type="password"
                        className="form-control"
                        id="password"
                        placeholder="Password"
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <label htmlFor="password">Password</label>
                </div>
                <div className="form-floating">
                    <input
                        type="password"
                        className="form-control"
                        id="passwordConfirm"
                        placeholder="Confirm Password"
                        onChange={(e) => setPasswordConfirm(e.target.value)}
                    />
                    <label htmlFor="confirmPassword">Confirm Password</label>
                </div>

                <button className="w-100 btn btn-lg btn-primary" type="submit">
                    Register
                </button>
            </form>
        </main>
    );
};
