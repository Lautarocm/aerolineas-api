"use client"

import styles from "./ResultsModifiers.module.css"
import { SortCheckbox } from "../SortCheckbox/SortCheckbox"
import { DropdownFilters } from "../DropdownFilters/DropdownFilters"
import { useSort } from "@/app/hooks/useSort"
import { useFilter } from "@/app/hooks/useFilter"
import { useContext } from "react"
import { FlightsContext } from "@/app/context/FlightsContext"

export function ResultsModifiers(){

    const {offersExist} = useContext(FlightsContext)
    const {handleSort} = useSort()
    const {handleFilter} = useFilter()
    const {sorted, filtered} = useContext(FlightsContext)

    return(
        <div className={styles.searchButtons}>
            <SortCheckbox className={styles.sort} handleSort={handleSort} sortDisabled={!offersExist} sorted={sorted} />
            <DropdownFilters className={styles.filter} handleFilter={handleFilter} filterDisabled={!offersExist} filtered={filtered} />
        </div>
    )
}