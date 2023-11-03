const baseURL = 'http://localhost:3030/jsonstore/todos'


export async function GetAllTask() {
    try {
        const response = await fetch(baseURL)

        const result = await response.json()

        const data = Object.values(result)

        return data
    }
    catch (error){
        return error
    }
}


export async function UpdateStatus(id) {

    data = {
        isCompleted: true,
    }

    try {
        const response = await fetch( `${baseURL}/${id}`, {
            method: 'PUT',
            headers: {
                "Content-Type": "application/json",
              },
            body: JSON.stringify(data),
            }
        )

        const result = await response.json()

        return result
    }
    catch (error) {
        return error
    }
}

