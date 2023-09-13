"use client"

import { useSearch } from "@/app/hooks/useSearch"
import styles from "./SearchButtons.module.css"
import { Button } from "@nextui-org/react"
import { SortCheckbox } from "../SortCheckbox/SortCheckbox"
import { DropdownFilters } from "../DropdownFilters/DropdownFilters"
import { useContext } from "react"
import { FlightsContext } from "@/app/context/FlightsContext"

export function SearchButtons(){

    const {offersExist} = useContext(FlightsContext)
    const {handleSearch, disableSearch} = useSearch()

    return(
        <div className={styles.searchButtons}>
            <Button
            className={styles.button}
            onClick={handleSearch}
            color="primary"
            size="md"
            radius="md"
            isDisabled={disableSearch}
            >
                Buscar
            </Button>
            <SortCheckbox className={styles.sort} sortDisabled={!offersExist} />
            <DropdownFilters className={styles.filter} filterDisabled={!offersExist} />
        </div>
    )
}