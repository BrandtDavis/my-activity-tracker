import axios from "axios";
import { useParams } from "react-router-dom"
import { useEffect, useState } from "react";

import { ActivityStatCard } from "../components/ActivityStatCard";
import { ActivityStatCardProps } from "../interfaces/props/propsInterfaces";

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
    

    let activityCardGridData: ActivityStatCardProps[] = [
        {
            header: "Total Hours of Activity",
            body: "This is the total time you've spent doing activities.",
            data: 100,
            unit: "Hours"
        },
        {
            header: "Total Number of Activities",
            body: "This is the total number of activities you have recorded.",
            data: 0,
            unit: ""
        },
        {
            header: "Total KMs Run",
            body: "This is the total KMs run or trail run.",
            data: undefined,
            unit: ""
        },
        {
            header: "Total KMs Biked",
            body: "This is the total KMs biked.",
            data: undefined,
            unit: ""
        }
    ]

    return (
        <div className="h-100">
            <h1 className="pl-4">{athleteName}'s Dashboard</h1>
            <div className="mx-auto py-4 border-2 w-2/3">
                <ul className="flex flex-row gap-4 flex-wrap justify-center">
                    {
                        activityCardGridData.map((activityStat) => (
                            <li>
                                <ActivityStatCard 
                                    header={activityStat.header}
                                    body={activityStat.body}
                                    data={activityStat.data}
                                    unit={activityStat.unit}
                                />
                            </li>
                        ))
                    }
                </ul>
            </div>
        </div>
    );
};
