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


