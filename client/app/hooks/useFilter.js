import { useState } from "react"

export function useFilter() {

    const [filtered, setFiltered] = useState(false)
    const [months, setMonths] = useState(new Set())

    const handleFilter = (months) => {
        if(months.size > 0){
            setFiltered(true)
            setMonths(months)
            
        }
        else{setFiltered(false)}
    }

    const resetFilter = () => {
        setMonths(new Set())
        setFiltered(false)
    }

    const handleChange = (months) => {
        setMonths(months)
    }

  return {filtered, handleFilter, months, resetFilter, handleChange}
}
