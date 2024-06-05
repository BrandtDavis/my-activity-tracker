export const ProfilePage = () => {
    let firstName = "Brandt"
    let lastName = "davis"
    let email = "Brandt@test.com"

    return (
        <>
            <h1 className="flex ml-4 mt-4 text-xl">Profile</h1>
            <div className="border-2 mx-auto max-w-screen-md">
                {/* Why Does Label Need to be First? */}

                <div className="block mt-2">
                    <label className="float" htmlFor="first-name">First Name:</label>
                    <input className="shadow float" readOnly={true} id="first-name" value={firstName}></input>
                </div>

                <div className="block mt-2">
                    <label className="float" htmlFor="first-name">Last Name:</label>
                    <input className="text-l shadow" type="text" readOnly={true} id="last-name" value={lastName}></input>
                </div>

                <div className="block mt-2">
                    <label className="float" htmlFor="first-name">Email:</label>
                    <input className="text-l shadow" type="email" readOnly={true} id="email" value={email}></input>
                </div>

            </div>
        </>
    )
}