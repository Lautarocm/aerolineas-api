import { useState, useEffect } from "react";
import { getAirports } from "../services/airports";

export function useAirports(){

    const [airports, setAirports] = useState([])

    useEffect(() => {
        getAirports().then(setAirports)
    }, [])

    return {airports}
}