import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';

export const UserActivityChart = (activityData: any) => {

  const data = [
    {date: 'Page A', uv: 400, amt: 5},
    {date: 'Page B', uv: 100, pv: 2400},
    {date: 'Page C', uv: 250, pv: 2400, amt: 2400},
    {date: 'Page C', uv: 250, pv: 2400, amt: 2400},
  ];
  
    const renderLineChart = (
        <LineChart width={600} height={300} data={data}>
          <Line type="monotone" dataKey="uv" stroke="#8884d8" />
          <CartesianGrid stroke="#ccc" />
          <XAxis dataKey="date" />
          <YAxis />
        </LineChart>
    );

    return (
      <div className="grow border-2 px-2">
        {renderLineChart}
      </div>
    );
}