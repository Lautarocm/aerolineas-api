"use client"

import { createContext, useEffect, useState } from "react"

export const FlightsContext = createContext({})

export default function FlightsProvider({children}){

    const [offers, setOffers] = useState([])
    const [loading, setLoading] = useState(false)
    const [filtered, setFiltered] = useState(false)
    const [sorted, setSorted] = useState(false)
    const [months, setMonths] = useState([])
    const [offersExist, setOffersExist] = useState(false)

    useEffect(() => {
        if(Array.isArray(offers)){
            offers.length > 0 && setOffersExist(true)
        }
    }, [offers])

    return (
        <FlightsContext.Provider value={{offers, setOffers, setLoading, loading, filtered, setFiltered, sorted, setSorted, months, setMonths, offersExist, setOffersExist}}>
            {children}
        </FlightsContext.Provider>
    )
}