"use client"

import { createContext, useState, useEffect } from "react"

export const FlightsContext = createContext({})

export default function FlightsProvider({children}){

    const [offers, setOffers] = useState([])
    const [offersExist, setOffersExist] = useState(false)
    const [origin, setOrigin] = useState("")
    const [destination, setDestination] = useState("")
    
    useEffect(() => {
        if(Array.isArray(offers)){
            offers.length > 0 && setOffersExist(true)
        }
    }, [offers])

    return (
        <FlightsContext.Provider value={{offers, offersExist, setOffers, setOffersExist, setOrigin, setDestination, origin, destination}}>
            {children}
        </FlightsContext.Provider>
    )
}