import { useContext, useEffect, useState } from "react"
import { useFilter } from "./useFilter"
import { useSort } from "./useSort"
import { FlightsContext } from "../context/FlightsContext"

export function useSortFilter(){

    const [offersToShow, setOffersToShow] = useState([])
    const {sorted, filtered, months, offers} = useContext(FlightsContext)
    const {sortOffers} = useSort()
    const {filterOffers} = useFilter()
    const {offersExist} = useContext(FlightsContext)

    const  sortAndFilter = () => {
        if(sorted && filtered){
            const filteredOffers = filterOffers(offers)
            const sortedOffers = sortOffers(filteredOffers)
            console.log("1")
            setOffersToShow(sortedOffers)
        }
        else if(filtered && !sorted){
            const filteredOffers = filterOffers(offers)
            console.log("2")
            setOffersToShow(filteredOffers)
        }
        else if(sorted && !filtered){
            const sortedOffers = sortOffers(offers)
            console.log("3")
            setOffersToShow(sortedOffers)
        }
        else{
            console.log("4")
            setOffersToShow(offers)
        }
    }
    useEffect(() => {
        offersExist && sortAndFilter()
    },[offers, filtered, sorted, months, offersExist])

    return{offersToShow}
}