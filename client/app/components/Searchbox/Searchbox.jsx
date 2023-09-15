import { useSelect } from "@/app/hooks/useSelect"
import styles from "./Searchbox.module.css"
import { CustomSelect } from "../CustomSelect/CustomSelect"
import { ResultsModifiers } from "../ResultsModifiers/ResultsModifiers"
import { useSearch } from "@/app/hooks/useSearch"
import { Button } from "@nextui-org/react"

export function Searchbox(){

    const {handleOrigin, handleDestination, origin, destination} = useSelect()
    const {handleSearch, disableSearch} = useSearch(origin, destination)

    return(
        <div className={styles.filtersContainer}>
            <CustomSelect
            className={styles.select}
            onChange={handleOrigin} label="Origen" />
            <CustomSelect
            className={styles.select}
            onChange={handleDestination} label="Destino" />
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
            <ResultsModifiers />
        </div>
    )
}