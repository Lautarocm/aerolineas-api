import { useSelect } from "@/app/hooks/useSelect"
import styles from "./Searchbox.module.css"
import { CustomSelect } from "../CustomSelect/CustomSelect"
import { useSearch } from "@/app/hooks/useSearch"
import { Button } from "@nextui-org/react"
import { SortCheckbox } from "../SortCheckbox/SortCheckbox"
import { DropdownFilters } from "../DropdownFilters/DropdownFilters"
import { useSort } from "@/app/hooks/useSort"
import { useFilter } from "@/app/hooks/useFilter"
import { useContext } from "react"
import { FlightsContext } from "@/app/context/FlightsContext"

export function Searchbox(){

    const {handleOrigin, handleDestination, origin, destination} = useSelect()
    const {handleSearch, disableSearch} = useSearch(origin, destination)
    const {offersExist, sorted, filtered} = useContext(FlightsContext)
    const {handleSort} = useSort()
    const {handleFilter} = useFilter()

    return(
        <div className={styles.filtersContainer}>
            <CustomSelect
            className={styles.select}
            onChange={handleOrigin} label="Origen" />
            <CustomSelect
            className={styles.select}
            onChange={handleDestination} label="Destino" />
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
                <SortCheckbox className={styles.sort} handleSort={handleSort} sortDisabled={!offersExist} sorted={sorted} />
                <DropdownFilters className={styles.filter} handleFilter={handleFilter} filterDisabled={!offersExist} filtered={filtered} />
            </div>
        </div>
    )
}