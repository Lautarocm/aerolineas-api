import { useContext, useState } from "react"
import { FlightsContext } from "../context/FlightsContext"

export function useFilter() {

    const {setFiltered, setMonths, months} = useContext(FlightsContext)

    const handleFilter = (months) => {
        setMonths(months)
        if(months.size > 0){
            setFiltered(true)
        }
        else{setFiltered(false)}
    }

    const resetFilter = () => {
        setMonths(new Set())
        setFiltered(false)
    }

    const filterOffers = (offers) => {
        const filteredOffers = offers.filter(offer => {
            return months.has(offer.departures[0].split("-")[1])
        })
        return filteredOffers
    }

  return {handleFilter, months, resetFilter, filterOffers}
}
