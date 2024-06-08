// import axios from "axios"
// let baseUrl = 'http://localhost:8000'
// // let baseUrl = `${import.meta.env.VITE_API_URL}`;
// export default defineEventHandler(async (event) => {
//     try {
//         const response = await axios.get(`${baseUrl}/api/v1/users?page=1`)
//         console.log('users?', response.data)
//         return {
//             data: response.data.results,
//             currentPage:1,
//             totalPages: response.data.num_pages,
//         };
//     } catch (e) {
//         console.log(e)
//     }
// })