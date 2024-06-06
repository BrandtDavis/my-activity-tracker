export const ProfilePage = () => {
    let firstName = "Brandt"
    let lastName = "Davis"
    let email = "Brandt@test.com"

    return (
        <>
            <h1 className="flex ml-4 mt-4 text-xl">Profile</h1>
            <div className="border mx-auto rounded shadow-md max-w-screen-md">
                {/* Why Does Label Need to be First? */}

                <div className="block ml-4 mt-2">
                    <label className="float" htmlFor="first-name">First Name:</label>
                    <input className="shadow float ml-2 pl-2" readOnly={true} id="first-name" value={firstName}></input>
                </div>

                <div className="block ml-4 mt-2">
                    <label className="float" htmlFor="last-name">Last Name:</label>
                    <input className="text-l shadow ml-2 pl-2" type="text" readOnly={true} id="last-name" value={lastName}></input>
                </div>

                <div className="block ml-4 mt-2">
                    <label className="float" htmlFor="email">Email:</label>
                    <input className="text-l shadow ml-2 pl-2" type="email" readOnly={true} id="email" value={email}></input>
                </div>

                <div className="block max-w-lg ml-12 mt-4 mb-4">
                    <input className="mx-auto px-4 py-1 rounded border-2 hover:cursoer" type="button" value="Back" />
                </div>
            </div>
        </>
    )
}