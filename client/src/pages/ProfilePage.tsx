import { useEffect, useState } from "react";
import { useParams } from "react-router-dom"
import axios from "axios";

export const ProfilePage = () => {

    const [athleteInfo, setAthleteInfo] = useState({
        first_name: "",
        last_name: "",
        email: "",
    });
    const { athleteId } = useParams();

    const url = `http://127.0.0.1:5000/athleteInfo?athlete_id=${athleteId}`;     
    

    useEffect(() => {
        axios.get(url, {
            headers: {
                'Content-type':'application/json', 
                'Accept':'application/json'
            },
        })
        .then((response) => {
            console.log(response)
            setAthleteInfo(response.data)
        }); 
    }, []);

    return (
        <>
            <h1 className="flex ml-4 mt-4 text-xl">Profile</h1>
            <div className="border mx-auto rounded shadow-md max-w-screen-md">
                {/* Why Does Label Need to be First? */}

                <div className="block ml-4 mt-2">
                    <label className="float" htmlFor="first-name">First Name:</label>
                    <input className="shadow float ml-2 pl-2" readOnly={true} id="first-name" value={athleteInfo.first_name}></input>
                </div>

                <div className="block ml-4 mt-2">
                    <label className="float" htmlFor="last-name">Last Name:</label>
                    <input className="text-l shadow ml-2 pl-2" type="text" readOnly={true} id="last-name" value={athleteInfo.last_name}></input>
                </div>

                <div className="block ml-4 mt-2">
                    <label className="float" htmlFor="email">Email:</label>
                    <input className="text-l shadow ml-2 pl-2" type="email" readOnly={true} id="email" value={athleteInfo.email}></input>
                </div>

                <div className="block max-w-lg ml-12 mt-4 mb-4">
                    <input className="mx-auto px-4 py-1 rounded border-2 hover:cursoer" type="button" value="Back" />
                </div>
            </div>
        </>
    )
}