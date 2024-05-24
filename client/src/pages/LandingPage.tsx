import React from "react";

export const LandingPage = () => {
    return (
        <div>
            <div>
                <h2>Enter Login Details</h2>
                <input className="" type="text" name="username" id="username" placeholder="username"/>
                <input className="" type="password" name="password" id="password" placeholder="password"/>
                <input className="" type="button" value={"Submit"}/>
            </div>
        </div>
    );
};
