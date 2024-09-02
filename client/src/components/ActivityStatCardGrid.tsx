import { Component } from "react"
import { ActivityStatCardProps } from "../interfaces/props/propsInterfaces";
import { ActivityStatCard } from "../components/ActivityStatCard";

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

export class ActivityStatCardGrid extends Component<{}, {}> {

    render() {
        return (
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
        )
    }
}
