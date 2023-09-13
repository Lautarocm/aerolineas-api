import { useContext, useState } from "react"
import { FlightsContext } from "../context/FlightsContext"

export function useSelect(){

    const {setOrigin, setDestination} = useContext(FlightsContext)

    const handleOrigin = (selectValue) => {
        setOrigin(selectValue)
    }

    const handleDestination = (selectValue) => {
        setDestination(selectValue)
    }

    return {handleOrigin, handleDestination}
}