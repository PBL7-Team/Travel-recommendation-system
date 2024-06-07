import axios from "axios"
// let baseUrl = 'http://localhost:8000'
let baseUrl = `${import.meta.env.VITE_API_URL}`;
export default defineEventHandler(async (event) => {
    try {
        const response = await axios.get(`${baseUrl}/api/v1/users/`)
        console.log('users?', response.data)
        return response.data;
    } catch (e) {
        console.log(e)
    }
})