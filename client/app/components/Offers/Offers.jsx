"use client"

import { DefaultMessage } from "../DefaultMessage/DefaultMessage"
import styles from "./Offers.module.css"
import { useSearch } from "@/app/hooks/useSearch"
import { useSortFilter } from "@/app/hooks/useSortFilter"
import { useSelect } from "@/app/hooks/useSelect"

export function Offers(){

    const {origin, destination} = useSelect()
    const {offersExist, offers, isSorted, isFiltered, months} = useSearch(origin, destination)
    const {offersToShow} = useSortFilter(offers, offersExist, isSorted, isFiltered, months)

    return(
        offersExist ?
        <ul className={styles.offers}>
            {offersToShow.map(offer => {
                return (
                    <li key={`${offer["id"]}`}><OfferCard offer={offer}></OfferCard></li>
                )
            })}
        </ul> :
        <DefaultMessage />
    )
}