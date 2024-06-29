import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const navigate = useNavigate();

    const loginUser = () => {
        if(username.length === 0){
            alert("Username is blank!");
        }
        else if(password.length === 0){
            alert("Password is blank!");
        }
        else {
            axios.post('http://127.0.0.1:5000/login', {
                email: username,
                password: password 
            })
            .then(function (response){
                if(response.status === 200) {
                    console.log(response.data)
                    let athleteId = response.data.athlete_id;
                    navigate(`/dashboard:${athleteId}`);
                }
            })
            .catch(function (error){
                console.log("Error: ", error);
            });
        }
    };

    return (
        <div>
            <div className="w-full max-w-md mx-auto mt-20">
            <form className="bg-white shadow-lg rounded px-8 pt-6 pb-8 mb-4">
                <h2 className="flex justify-center mb-4 text-xl font-bold">Strava dashboard</h2>

                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
                        username
                    </label>
                    <input 
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                      id="username" 
                      type="text" 
                      value={username} 
                      onChange={(e) => setUsername(e.target.value)} 
                      placeholder="username" 
                    />
                </div>
                <div className="mb-6">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
                        password
                    </label>
                    <input 
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" 
                      id="password" 
                      type="password" 
                      value={password}
                      onChange={(e) => setPassword(e.target.value)} 
                      placeholder="*********"
                    />
                    {/* <input className="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************"/> */}
                    {/* <p className="text-red-500 text-xs italic">Please choose a password.</p> */}
                </div>
                <div className="flex items-center justify-between">
                    <button 
                      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" 
                      type="button"
                      onClick={loginUser}
                    >
                        log in
                    </button>
                    <a className="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800" href="#">
                        forgot password?
                    </a>
                </div>
            </form>
            <p className="text-center text-gray-500 text-xs">
            </p>
            </div>
        </div>
    );
};
