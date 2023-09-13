export const getAirports = () => {
    return fetch("http://localhost:8080/airports")
    .then(res => res.json())
    .then(data => data)
}