const BaseUrl = 'http://localhost:3030/jsonstore/users';


export const GetAllUsers = async () => {
    try {
        const response = await fetch(BaseUrl);

        const result = await response.json();
        return Object.values(result);
    } catch (err) {
        console(err);
    }

}