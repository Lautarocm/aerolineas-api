import { useState, useContext, useEffect } from "react"
import { getOffers } from "../services/offers"
import { FlightsContext } from "../context/FlightsContext"
import { useSort } from "./useSort"
import { useFilter } from "./useFilter"

export function useSearch(origin, destination){

    const [disableSearch, setDisableSearch] = useState(true)
    const {setOffers, setLoading} = useContext(FlightsContext)
    const {resetSort} = useSort()
    const {resetFilter} = useFilter()
    const {setOffersExist} = useContext(FlightsContext)


    useEffect(() => {
        (origin && destination) && setDisableSearch(false)
    },[origin, destination])

    const handleSearch = () => {
        
        const queryParams = []
        origin != "" && queryParams.push(`origin=${origin}`)
        destination != "" && queryParams.push(`destination=${destination}`)
        const query = queryParams.join("&")
        const url = `http://localhost:8080/scrape?${query}`

        setLoading(true)
        resetFilter()
        resetSort()
        setOffersExist(false)
        getOffers(url).then(setOffers).finally(() => setLoading(false))
    }

    return {handleSearch, disableSearch}
}