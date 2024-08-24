import { Component } from "react"

export class ActivityWeekSelector extends Component {

    render() {
        return (
            <>
                <div className="inline-block">
                    <input type="radio" id="2-week-radio-btn" value="" className="appearance-none"/>
                    <label htmlFor="2-week-radio-btn" className="border-2 px-2">2 Weeks</label>

                    <input type="radio" id="4-week-radio-btn" className="appearance-none" />
                    <label htmlFor="4-week-radio-btn" className="border-2 px-2">4 Weeks</label>

                    <input type="radio" id="8-week-radio-btn" className="appearance-none" />
                    <label htmlFor="8-week-radio-btn"className="border-2 px-2">8 Weeks</label>
                </div>
            </>
        )
    }
}
