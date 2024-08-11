import { Component } from "react"

export class ActivityWeekSelector extends Component {

    render() {
        return (
            <>
                <div className="inline-block">
                    <input type="radio" id="2-week-radio-btn" value="" />
                    <label htmlFor="2-week-radio-btn">2 Weeks</label>

                    <input type="radio" id="4-week-radio-btn" />
                    <label htmlFor="4-week-radio-btn">4 Weeks</label>

                    <input type="radio" id="8-week-radio-btn" />
                    <label htmlFor="8-week-radio-btn">8 Weeks</label>
                </div>
            </>
        )
    }
}
