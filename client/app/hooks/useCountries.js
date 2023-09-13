import { useState, useEffect } from "react"
import { getAirports } from "../services/airports"

export function useCountries(airports){
    
    const [countries, setCountries] = useState([])

    useEffect(() => {
        const countries = new Set(airports.map(airport => airport.city.country.name))
        setCountries(Array.from(countries))
    },[airports])

    return {countries}
}