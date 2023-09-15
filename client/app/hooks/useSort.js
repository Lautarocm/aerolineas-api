import { useContext, useState } from "react"
import { FlightsContext } from "../context/FlightsContext"

export function useSort() {

    const {setSorted} = useContext(FlightsContext)

    const handleSort = () => {
      setSorted(state => !state
      )
    }

    const resetSort = () => {
      setSorted(false)
    }

    const sortOffers = (offers) => {
      const sortedOffers = offers.slice().sort((a, b)=>a["price"]-b["price"])
      return sortedOffers
    }

  return {handleSort, resetSort, sortOffers}
}
