import { useState, useContext, useEffect } from "react"
import { getOffers } from "../services/offers"
import { FlightsContext } from "../context/FlightsContext"
import { useSort } from "./useSort"
import { useFilter } from "./useFilter"

export function useSearch(){

    const [loading, setLoading] = useState(false)
    const [disableSearch, setDisableSearch] = useState(true)
    const {setOffersExist, setOffers, origin, destination} = useContext(FlightsContext)
    const {resetSort} = useSort()
    const {resetFilter} = useFilter()


    useEffect(() => {
        (origin && destination) && setDisableSearch(false)
    })

    const handleSearch = () => {
        
        const queryParams = []
        origin != "" && queryParams.push(`origin=${origin}`)
        destination != "" && queryParams.push(`destination=${destination}`)
        const query = queryParams.join("&")
        const url = `http://localhost:8080/scrape?${query}`

        resetFilter()
        resetSort()
        setOffersExist(false)
        setLoading(true)
        getOffers(url).then(setOffers).finally(() => setLoading(false))
    }

    return {handleSearch, loading, disableSearch}
}