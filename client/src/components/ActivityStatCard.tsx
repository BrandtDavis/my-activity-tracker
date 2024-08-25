import { Component } from "react"

interface ActivityStatCardProps {
    header: string
    body: string
    data?: number
    unit?: string
}
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
                <div className="max-w-sm rounded overflow-hidden shadow-lg">
                <img className="w-full" src="" alt="Clock icon"/>
                <div className="px-6 py-4">
                    <div className="font-bold text-xl mb-2">{this.props.header}</div>
                    <p className="text-gray-700 text-base">{this.props.body}</p>
                    <span className="align-middle mx-auto">{dataText}</span>
                </div>
                <div className="px-6 pt-4 pb-2">
                </div>
                </div>
            </>
        )
    }
}
