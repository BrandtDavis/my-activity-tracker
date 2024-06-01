import React from "react";

import { LineChart, Line } from 'recharts';
const data = [{name: 'Page A', uv: 400, pv: 2400, amt: 2400}];

const renderLineChart = (
  <LineChart width={400} height={400} data={data}>
    <Line type="monotone" dataKey="uv" stroke="#8884d8" />
  </LineChart>
);

export const DashboardPage = () => {

    return (
        <div>
            <h1 className="pl-4">Brandt's Dashboard</h1>
            <div className="container mx-auto border-2 px-4 py-4">
                <div className="grow border-2 px-2">
                   {renderLineChart}
                </div>
            </div>
        </div>
    );
};
