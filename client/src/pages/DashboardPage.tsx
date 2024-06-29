import axios from "axios";
import React from "react";
import { useParams } from "react-router-dom"
import { useEffect, useState } from "react";

import { UserActivityChart } from "../components/UserActivityChart";

export const DashboardPage = () => {

    const [athleteName, setAthleteName] = useState("");
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
          setAthleteName(response.data.first_name)
      }); 
    }, []);
    
    return (
        <div className="h-100">
            <h1 className="pl-4">{athleteName}'s Dashboard</h1>
            <div className="container mx-auto border-2 px-4 py-4">
              <UserActivityChart athleteId={athleteId}/>
            </div>
        </div>
    );
};
