import axios from "axios";
import { useParams } from "react-router-dom"
import { useEffect, useState } from "react";

import { ActivityStatCardGrid } from "../components/ActivityStatCardGrid";

export const DashboardPage = () => {

    const [athleteName, setAthleteName] = useState("");
    const { athleteId } = useParams();

    // Populate Athlethe Name
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

    // Populate Athlete Activity Stats
    const totalHoursUrl: string = ``;
    axios.get(url, {
        headers: {

        },
    }).then((response) => {
        // 
    });
    


    return (
        <div className="h-100">
            <h1 className="pl-4">{athleteName}'s Dashboard</h1>
            <div className="mx-auto py-4 border-2 w-2/3">
                <ActivityStatCardGrid />
            </div>
        </div>
    );
};
