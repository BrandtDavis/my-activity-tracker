import { Component } from "react"
import { ActivityStatCardProps } from "../interfaces/props/propsInterfaces";
export class ActivityStatCard extends Component<ActivityStatCardProps, {}> {

    render() {
        let dataText: string = '';
        if (this.props.data === undefined || this.props.unit === undefined) {
            dataText = `Data Unavailable`;
        }
        else {
            dataText = `${this.props.data} ${this.props.unit}`
        }

        return (
            <>
                <div className="mx-auto col-span-1 w-32 md:w-72 lg:w-96 h-fit bg-gray-100 hover:bg-base-200 max-w-sm rounded overflow-hidden shadow-lg">
                    <div className="px-6 py-4 center">
                        <div className="font-bold text-xl mb-2">{this.props.header}</div>
                        <p className="text-gray-700 text-base">{this.props.body}</p>
                    </div>
                    <div className="px-6 pt-4 pb-2">
                        <span className="align-middle font-bold">{dataText}</span>
                    </div>
                </div>
            </>
        )
    }
}
