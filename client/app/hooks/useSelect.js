import { useState } from "react"

export function useSelect(){

    const [origin, setOrigin] = useState("")
    const [destination, setDestination] = useState("")

    const handleOrigin = (selectValue) => {
        setOrigin(selectValue)
    }

    const handleDestination = (selectValue) => {
        setDestination(selectValue)
    }

    return {handleOrigin, handleDestination, origin, destination}
}