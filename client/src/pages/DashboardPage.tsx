import axios from "axios";
import { useParams } from "react-router-dom"
import { useEffect, useState } from "react";

import { ActivityStatCard } from "../components/ActivityStatCard";

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

                <ActivityStatCard 
                  header="Total Hours of Activity"
                  body="This is the total time you've spent doing activities."
                  data={100}
                  unit={"Hours"}
                />

                <ActivityStatCard 
                  header="Total Number of Activities"
                  body="This is the total number of activities you have recorded."
                />

                <ActivityStatCard 
                  header="Total KMs Run"
                  body="This is the total KMs run or trail run."
                />

                <ActivityStatCard 
                  header="Total KMs"
                  body="This is the total KMs biked."
                />
            </div>
        </div>
    );
};
