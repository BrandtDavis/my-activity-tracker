import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';
import React, { useState, useEffect } from "react";
import axios from "axios";

import CustomizedXAxisTick from '../components/graph/CustomXAxisTick';

export const UserActivityChart = (athleteId: any) => {

  const [activityData, setActivityData] = useState(
    [
      {
        date: '',
        distance: 0,
      }
    ]
  );

  const url = `http://127.0.0.1:5000/athlete_activities?athlete_id=${athleteId.athleteId}`

  useEffect(() => {
    axios.get(url, {
      headers: {
        'Content-type':'application/json', 
        'Accept':'application/json'
      },
    })
    .then((response) => {
      let activities = response.data.activities.map((activity: {week: string, date: string, distance: number}) => {
        activity.date = activity.date.split('T')[0];
        activity.distance = activity.distance / 1000;
        return activity;
      });

      setActivityData(activities)
    });
  }, []);

    const renderLineChart = (
        <LineChart width={600} height={300} data={activityData}>
          <Line type="monotone" dataKey="distance" stroke="#8884d8" />
          <CartesianGrid stroke="#ccc" />
          <XAxis dataKey="date" tick={<CustomizedXAxisTick x={0} y={0} stroke={null} payload="date" />}/>
          <YAxis />
        </LineChart>
    );

    return (
      <div className="grow border-2 px-2">
        {renderLineChart}
      </div>
    );
}