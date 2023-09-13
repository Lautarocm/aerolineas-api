import { useState, useEffect, useContext } from "react"
import { FlightsContext } from "../context/FlightsContext"
import { useFilter } from "./useFilter"
import { useSort } from "./useSort"

export function useSortFilter(){

    const [offersToShow, setOffersToShow] = useState([])
    const {offers, offersExist} = useContext(FlightsContext)
    const {sorted} = useSort()
    const {filtered, months} = useFilter()

    const sortOffers = (offers) => {
        const sortedOffers = offers.slice().sort((a, b)=>a["price"]-b["price"])
        return sortedOffers
    }

    const filterOffers = (offers) => {
        const filteredOffers = offers.filter(offer => {
            return months.has(offer.departures[0].split("-")[1])
        })
        return filteredOffers
    }

    const sortAndFilter = (offers) => {
        if(sorted && filtered){
            const filteredOffers = filterOffers(offers)
            const sortedOffers = sortOffers(filteredOffers)
            setOffersToShow(sortedOffers)
            console.log("1")
        }
        else if(filtered && !sorted){
            const filteredOffers = filterOffers(offers)
            setOffersToShow(filteredOffers)
            console.log("2")
        }
        else if(sorted && !filtered){
            const sortedOffers = sortOffers(offers)
            setOffersToShow(sortedOffers)
            console.log("3")
        }
        else{
            setOffersToShow(offers)
            console.log("4")
        }
    }

    useEffect(() => {
        offersExist && sortAndFilter(offers)
    }, [offers, sorted, filtered, months, offersExist])

    return{offersToShow}
}